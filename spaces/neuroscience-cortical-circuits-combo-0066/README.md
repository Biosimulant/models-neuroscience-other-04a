# COMBO_0066 - Neuroscience Cortical Circuits

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
- `neuroscience-other-cerebellar-nuclear-neuron-sudhakar-et-al-2015-185513-model`: Neuroscience: CerebellarNuclearNeuronSudhakarEtAl2015185513Model
- `neuroscience-other-cerebellar-optokinetic-response-osb267334-model`: Neuroscience: Model267334267334Model
- `neuroscience-other-cerebellar-parallel-fiber-purkinje-cell-ltd-ltp-osb235376-model`: Neuroscience: Model235376235376Model
- `neuroscience-other-cerebellar-phase-locked-tacs-essential-tremor-osb266842-model`: Neuroscience: Model266842266842Model

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
- neuroscience-other-cerebellar-nuclear-neuron-sudhakar-et-al-2015-185513-model :: modeldb:185513 :: https://modeldb.science/185513
- neuroscience-other-cerebellar-optokinetic-response-osb267334-model :: opensourcebrain:267334 :: https://github.com/OpenSourceBrain/267334
- neuroscience-other-cerebellar-parallel-fiber-purkinje-cell-ltd-ltp-osb235376-model :: opensourcebrain:235376 :: https://github.com/OpenSourceBrain/235376
- neuroscience-other-cerebellar-phase-locked-tacs-essential-tremor-osb266842-model :: opensourcebrain:266842 :: https://github.com/OpenSourceBrain/266842

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
