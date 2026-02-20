# COMBO_0060 - Neuroscience Cortical Circuits

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
- `neuroscience-other-calculating-consequences-left-shifted-nav-channel-activity-sick-cells-osb234111-model`: Neuroscience: Model234111234111Model
- `neuroscience-other-cannula-artifact-osb230888-model`: Neuroscience: Model230888230888Model
- `neuroscience-other-cardiac-models-circadian-rhythms-early-afterdepolarizations-arrhythmias-osb266974-model`: Neuroscience: Model266974266974Model
- `neuroscience-other-cat-locomotion-paw-shaking-central-pattern-generator-osb267219-model`: Neuroscience: Model267219267219Model

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
- neuroscience-other-calculating-consequences-left-shifted-nav-channel-activity-sick-cells-osb234111-model :: opensourcebrain:234111 :: https://github.com/OpenSourceBrain/234111
- neuroscience-other-cannula-artifact-osb230888-model :: opensourcebrain:230888 :: https://github.com/OpenSourceBrain/230888
- neuroscience-other-cardiac-models-circadian-rhythms-early-afterdepolarizations-arrhythmias-osb266974-model :: opensourcebrain:266974 :: https://github.com/OpenSourceBrain/266974
- neuroscience-other-cat-locomotion-paw-shaking-central-pattern-generator-osb267219-model :: opensourcebrain:267219 :: https://github.com/OpenSourceBrain/267219

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
