# Space Plan - neuroscience-cortical-circuits-combo-0059

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-ca2-oscillations-single-astrocytes-osb223144-model, neuroscience-other-ca2-oscillations-sympathetic-neurons-osb247655-model, neuroscience-other-ca2-requirements-long-term-depression-purkinje-cells-osb245412-model, neuroscience-other-calcium-spikes-in-basal-dendrites-kampa-and-stua-108458-model

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
