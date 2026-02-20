# COMBO_0070 - Neuroscience Hippocampal Circuits

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
- `neuroscience-other-calcium-waves-and-mglur-dependent-synaptic-plast-150551-model`: Neuroscience: CalciumWavesAndMglurDependentSynapticPlast150551Model
- `neuroscience-other-calcium-waves-mglur-dependent-synaptic-plasticity-ca1-pyr-osb150551-model`: Neuroscience: Model150551150551Model
- `neuroscience-other-changes-of-ionic-concentrations-during-seizure-t-222321-model`: Neuroscience: ChangesOfIonicConcentrationsDuringSeizureT222321Model
- `neuroscience-other-channel-density-variability-among-ca1-neurons-mi-244688-model`: Neuroscience: ChannelDensityVariabilityAmongCa1NeuronsMi244688Model

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
- neuroscience-other-calcium-waves-and-mglur-dependent-synaptic-plast-150551-model :: modeldb:150551 :: https://modeldb.science/150551
- neuroscience-other-calcium-waves-mglur-dependent-synaptic-plasticity-ca1-pyr-osb150551-model :: opensourcebrain:150551 :: https://github.com/OpenSourceBrain/150551
- neuroscience-other-changes-of-ionic-concentrations-during-seizure-t-222321-model :: modeldb:222321 :: https://modeldb.science/222321
- neuroscience-other-channel-density-variability-among-ca1-neurons-mi-244688-model :: modeldb:244688 :: https://modeldb.science/244688

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
