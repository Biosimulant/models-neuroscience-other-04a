# COMBO_0031 - Neuroscience Hippocampal Circuits

## Scientific Question
How do recurrent hippocampal motifs shape network dynamics over time?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-ca3-pyramidal-cell-osb35358-model`: Neuroscience: Model3535835358Model
- `neuroscience-other-ca3-pyramidal-neuron-firing-properties-hemond-et-101629-model`: Neuroscience: Ca3PyramidalNeuronFiringPropertiesHemondEt101629Model
- `neuroscience-other-ca3-pyramidal-neuron-membrane-response-near-rest-118098-model`: Neuroscience: Ca3PyramidalNeuronMembraneResponseNearRest118098Model

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
- neuroscience-other-ca3-pyramidal-cell-osb35358-model :: opensourcebrain:35358 :: https://github.com/OpenSourceBrain/35358
- neuroscience-other-ca3-pyramidal-neuron-firing-properties-hemond-et-101629-model :: modeldb:101629 :: https://modeldb.science/101629
- neuroscience-other-ca3-pyramidal-neuron-membrane-response-near-rest-118098-model :: modeldb:118098 :: https://modeldb.science/118098

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
