# Space Plan - neuroscience-cortical-circuits-combo-0060

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-calculating-consequences-left-shifted-nav-channel-activity-sick-cells-osb234111-model, neuroscience-other-cannula-artifact-osb230888-model, neuroscience-other-cardiac-models-circadian-rhythms-early-afterdepolarizations-arrhythmias-osb266974-model, neuroscience-other-cat-locomotion-paw-shaking-central-pattern-generator-osb267219-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
