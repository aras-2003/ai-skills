from pathlib import Path
import json
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from prepare_closure import assemble, prepare, validate


class ClosurePackTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.out = Path(self.temp.name) / 'pack'
        self.summary = prepare(self.out)

    def test_all_entrypoints_and_workflows(self):
        self.assertEqual(self.summary['components'], 70)
        self.assertEqual(self.summary['skills'], 54)
        self.assertEqual(self.summary['workflows'], 16)
        self.assertEqual(self.summary['by_lane']['workflow'], 48)
        self.assertEqual(self.summary['by_lane']['loader-parity'], 70)

    def test_full_backlog_and_no_runtime_pass(self):
        self.assertEqual(self.summary['backlog_items'], 89)
        self.assertEqual(self.summary['runtime_tests_executed'], 0)
        q = json.loads((self.out / 'queue.json').read_text())['cases']
        self.assertTrue(all(c['status'] == 'NOT_RUN' and c['outcome'] is None for c in q))

    def test_executor_has_only_opaque_input_files(self):
        with zipfile.ZipFile(self.out / 'executor-inputs.zip') as z:
            self.assertEqual(len(z.namelist()), self.summary['case_count'])
            self.assertTrue(all(n.removesuffix('.input.md').isdigit() for n in z.namelist()))
            self.assertFalse(any('rubric' in n or 'queue' in n for n in z.namelist()))

    def test_inputs_tamper_detected(self):
        next((self.out / 'executor').glob('*.input.md')).write_text('changed')
        with self.assertRaisesRegex(ValueError, 'digest mismatch'):
            validate(self.out)

    def test_rubric_tamper_detected(self):
        next((self.out / 'evaluator').glob('*.json')).write_text('{}')
        with self.assertRaisesRegex(ValueError, 'digest mismatch'):
            validate(self.out)

    def test_archive_leak_detected(self):
        with zipfile.ZipFile(self.out / 'executor-inputs.zip', 'a') as z:
            z.writestr('rubric.json', '{}')
        with self.assertRaisesRegex(ValueError, 'isolation'):
            validate(self.out)

    def test_preparation_cannot_claim_pass(self):
        path = self.out / 'queue.json'
        data = json.loads(path.read_text())
        data['cases'][0]['status'] = 'PASS'
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'runtime results'):
            validate(self.out)

    def test_never_overwrite_evidence(self):
        with self.assertRaisesRegex(ValueError, 'preserve previous evidence'):
            prepare(self.out)

    def test_reproducible_pack(self):
        other = Path(self.temp.name) / 'second'
        prepare(other)
        for name in ('queue.json', 'summary.json', 'coverage.json', 'BACKLOG.md', 'executor-inputs.zip', 'orchestrator-handoff.zip'):
            self.assertEqual((self.out / name).read_bytes(), (other / name).read_bytes())

    def test_refinements_and_overlay_are_not_historical_pass(self):
        _, _, cases = assemble()
        self.assertEqual(self.summary['fixture_review_count'], 0)
        self.assertEqual(self.summary['refined_legacy_fixtures'], 38)
        overlays = [c for c in cases if c['rubric'].get('profile_overlay')]
        self.assertEqual(len(overlays), 2)
        self.assertTrue(all('not a historical' in c['rubric']['profile_overlay'] for c in overlays))

    def test_all_write_cases_guarded(self):
        q = json.loads((self.out / 'queue.json').read_text())['cases']
        self.assertTrue(all(c['writes'] == 'forbidden-in-real-systems' for c in q))
        guarded = [c for c in q if 'investment' in c['target'] or c['target'] == 'decision-journal-update']
        self.assertTrue(all(c['integration_write_gate'] == 'isolated-test-store-required' for c in guarded))


if __name__ == '__main__':
    unittest.main()
