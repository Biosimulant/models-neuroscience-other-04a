# COMBO_0073 - Neuroscience Cortical Circuits

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
- `neuroscience-other-cerebellum-granule-cell-fhf-dover-et-al-2016-206267-model`: Neuroscience: CerebellumGranuleCellFhfDoverEtAl2016206267Model
- `neuroscience-other-cerebellum-granule-cell-fhf-osb206267-model`: Neuroscience: Model206267206267Model
- `neuroscience-other-cerebellum-purkinje-cell-osb244679-model`: Neuroscience: Model244679244679Model
- `neuroscience-other-changes-ionic-concentrations-during-seizure-transitions-osb222321-model`: Neuroscience: Model222321222321Model

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
- neuroscience-other-cerebellum-granule-cell-fhf-dover-et-al-2016-206267-model :: modeldb:206267 :: https://modeldb.science/206267
- neuroscience-other-cerebellum-granule-cell-fhf-osb206267-model :: opensourcebrain:206267 :: https://github.com/OpenSourceBrain/206267
- neuroscience-other-cerebellum-purkinje-cell-osb244679-model :: opensourcebrain:244679 :: https://github.com/OpenSourceBrain/244679
- neuroscience-other-changes-ionic-concentrations-during-seizure-transitions-osb222321-model :: opensourcebrain:222321 :: https://github.com/OpenSourceBrain/222321

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
