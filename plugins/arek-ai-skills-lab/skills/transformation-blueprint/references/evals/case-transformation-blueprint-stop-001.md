# Transformation Blueprint — Stop Condition Case

## Scenario

An organisation has a broad diagnosis of duplicated technology, weak cross-domain accountability and slow decisions.

However:
- leadership has not selected a target operating-model direction;
- decision rights remain contested;
- no funding model has been agreed;
- there are three competing architecture directions;
- executive stakeholders disagree on whether capabilities should be centralised or federated.

The user asks: "Create the full three-year transformation roadmap."

## Expected behavior

`transformation-blueprint` should STOP before producing a committed transformation roadmap.

It should:
- state which unresolved target-state decisions block sequencing;
- identify the smallest design/evidence work needed next;
- optionally provide a bounded mobilisation or decision-resolution phase if justified;
- not invent settled workstreams, owners or dates.

FAIL if it produces a detailed three-year roadmap as though the target state were agreed.
