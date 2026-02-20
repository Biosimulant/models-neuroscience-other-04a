# COMBO_0059 - Neuroscience Cortical Circuits

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
- `neuroscience-other-ca2-oscillations-single-astrocytes-osb223144-model`: Neuroscience: Model223144223144Model
- `neuroscience-other-ca2-oscillations-sympathetic-neurons-osb247655-model`: Neuroscience: Model247655247655Model
- `neuroscience-other-ca2-requirements-long-term-depression-purkinje-cells-osb245412-model`: Neuroscience: Model245412245412Model
- `neuroscience-other-calcium-spikes-in-basal-dendrites-kampa-and-stua-108458-model`: Neuroscience: CalciumSpikesInBasalDendritesKampaAndStua108458Model

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
- neuroscience-other-ca2-oscillations-single-astrocytes-osb223144-model :: opensourcebrain:223144 :: https://github.com/OpenSourceBrain/223144
- neuroscience-other-ca2-oscillations-sympathetic-neurons-osb247655-model :: opensourcebrain:247655 :: https://github.com/OpenSourceBrain/247655
- neuroscience-other-ca2-requirements-long-term-depression-purkinje-cells-osb245412-model :: opensourcebrain:245412 :: https://github.com/OpenSourceBrain/245412
- neuroscience-other-calcium-spikes-in-basal-dendrites-kampa-and-stua-108458-model :: modeldb:108458 :: https://modeldb.science/108458

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
