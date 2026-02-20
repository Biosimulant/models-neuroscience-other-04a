# COMBO_0062 - Neuroscience Cortical Circuits

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
- `neuroscience-other-cellular-synaptic-mechanisms-differentiate-mitral-superficial-tufted-cells-osb267013-model`: Neuroscience: Model267013267013Model
- `neuroscience-other-central-nervous-system-tadpole-matlab-neuron-python-osb267146-model`: Neuroscience: Model267146267146Model
- `neuroscience-other-cerebellar-basket-cell-model-masoli-et-al-2025-2018018-model`: Neuroscience: CerebellarBasketCellModelMasoliEtAl20252018018Model
- `neuroscience-other-cerebellar-basket-cell-osb2018018-model`: Neuroscience: Model20180182018018Model

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
- neuroscience-other-cellular-synaptic-mechanisms-differentiate-mitral-superficial-tufted-cells-osb267013-model :: opensourcebrain:267013 :: https://github.com/OpenSourceBrain/267013
- neuroscience-other-central-nervous-system-tadpole-matlab-neuron-python-osb267146-model :: opensourcebrain:267146 :: https://github.com/OpenSourceBrain/267146
- neuroscience-other-cerebellar-basket-cell-model-masoli-et-al-2025-2018018-model :: modeldb:2018018 :: https://modeldb.science/2018018
- neuroscience-other-cerebellar-basket-cell-osb2018018-model :: opensourcebrain:2018018 :: https://github.com/OpenSourceBrain/2018018

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
