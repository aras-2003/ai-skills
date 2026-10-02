# Canonical schema governance

## Purpose
Make the Supabase canonical target unambiguous before any Investment OS read or write.

## Bootstrap authority
The bootstrap location is fixed:

- project: configured Investment OS Supabase project
- schema: `public`
- table: `system_config`
- required key: `canonical_backend`
- optional policy key: `canonical_schema_policy`

The bootstrap location is metadata only. It exists so the runtime can discover the active canonical schema without scanning multiple schemas or guessing from populated tables.

## Canonical schema resolution
1. Read `public.system_config` first.
2. Resolve `canonical_backend` and require:
   - backend = `SUPABASE`;
   - project_id matches the connected Investment OS project;
   - schema is non-empty;
   - cutover is true for post-cutover operation.
3. If `canonical_schema_policy` exists, require:
   - status = `ACTIVE`;
   - bootstrap_schema = `public`;
   - bootstrap_table = `system_config`;
   - bootstrap_key = `canonical_backend`;
   - canonical_schema matches `canonical_backend.schema`;
   - cross_schema_fallback = false.
4. Use only the resolved canonical schema for normalized Investment OS reads and writes.
5. Do not scan another schema for equivalent tables when the canonical schema is empty, missing data or unavailable.
6. A noncanonical schema may be inspected only for migration/security diagnostics and must be labeled NONCANONICAL.

## Current deployment
Current configured canonical target:
- backend: Supabase
- project name: `investment-os`
- canonical schema: `public`

The `investment` schema is deprecated/noncanonical. Its contents, configuration or row counts must never override `public.system_config`.

## Failure states
Return `UNAVAILABLE` or `FAILED` instead of guessing when:
- bootstrap metadata cannot be read;
- canonical project ID does not match the connected project;
- canonical schema is missing;
- policy and backend metadata disagree;
- cross-schema fallback would be required to satisfy the request.

## Migration and cutover
A future schema migration must be explicit:
1. populate and reconcile the target schema;
2. validate row counts, keys, policy/thesis chronology and latest portfolio state;
3. record a cutover event;
4. atomically update `public.system_config.canonical_backend.schema` and `canonical_schema_policy.canonical_schema`;
5. only then allow reads/writes against the new schema.

Never infer cutover from which schema happens to contain rows.
