# Space Plan - neuroscience-cortical-circuits-combo-0062

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-cellular-synaptic-mechanisms-differentiate-mitral-superficial-tufted-cells-osb267013-model, neuroscience-other-central-nervous-system-tadpole-matlab-neuron-python-osb267146-model, neuroscience-other-cerebellar-basket-cell-model-masoli-et-al-2025-2018018-model, neuroscience-other-cerebellar-basket-cell-osb2018018-model

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
