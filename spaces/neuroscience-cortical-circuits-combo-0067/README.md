# COMBO_0067 - Neuroscience Cortical Circuits

## Scientific Question
How do cortical circuit motifs transform and propagate activity?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-cerebellar-stellate-cell-model-rizza-et-al-2021-2018019-model`: Neuroscience: CerebellarStellateCellModelRizzaEtAl20212018019Model
- `neuroscience-other-cerebellar-stellate-cell-osb2018019-model`: Neuroscience: Model20180192018019Model
- `neuroscience-other-cerebellar-stellate-cells-changes-in-threshold-l-266718-model`: Neuroscience: CerebellarStellateCellsChangesInThresholdL266718Model
- `neuroscience-other-cerebellar-stellate-cells-osb266718-model`: Neuroscience: Model266718266718Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- neuroscience-other-cerebellar-stellate-cell-model-rizza-et-al-2021-2018019-model :: modeldb:2018019 :: https://modeldb.science/2018019
- neuroscience-other-cerebellar-stellate-cell-osb2018019-model :: opensourcebrain:2018019 :: https://github.com/OpenSourceBrain/2018019
- neuroscience-other-cerebellar-stellate-cells-changes-in-threshold-l-266718-model :: modeldb:266718 :: https://modeldb.science/266718
- neuroscience-other-cerebellar-stellate-cells-osb266718-model :: opensourcebrain:266718 :: https://github.com/OpenSourceBrain/266718

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
