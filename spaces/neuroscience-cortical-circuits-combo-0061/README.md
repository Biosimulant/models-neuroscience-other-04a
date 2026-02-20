# COMBO_0061 - Neuroscience Cortical Circuits

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
- `neuroscience-other-cell-models-wiring-variations-that-enable-constrain-neural-computation-sensory-osbTobinEtAl2017-model`: Neuroscience: Tobinetal2017Tobinetal2017Model
- `neuroscience-other-cell-type-specific-integration-feedforward-feedback-synaptic-inputs-osb267509-model`: Neuroscience: Model267509267509Model
- `neuroscience-other-cellular-classes-revealed-heartbeat-related-modulation-extracellular-aps-osb263961-model`: Neuroscience: Model263961263961Model
- `neuroscience-other-cellular-function-given-parametric-variation-hh-excitability-osb262464-model`: Neuroscience: Model262464262464Model

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
- neuroscience-other-cell-models-wiring-variations-that-enable-constrain-neural-computation-sensory-osbTobinEtAl2017-model :: opensourcebrain:TobinEtAl2017 :: https://github.com/OpenSourceBrain/TobinEtAl2017
- neuroscience-other-cell-type-specific-integration-feedforward-feedback-synaptic-inputs-osb267509-model :: opensourcebrain:267509 :: https://github.com/OpenSourceBrain/267509
- neuroscience-other-cellular-classes-revealed-heartbeat-related-modulation-extracellular-aps-osb263961-model :: opensourcebrain:263961 :: https://github.com/OpenSourceBrain/263961
- neuroscience-other-cellular-function-given-parametric-variation-hh-excitability-osb262464-model :: opensourcebrain:262464 :: https://github.com/OpenSourceBrain/262464

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
