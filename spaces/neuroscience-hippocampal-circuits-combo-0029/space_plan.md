# Space Plan - neuroscience-hippocampal-circuits-combo-0029

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-ca3-hippocampal-pyramidal-neuron-voltage-clamp-intrinsic-conductance-data-osb266905-model, neuroscience-other-ca3-hippocampal-pyramidal-neuron-with-voltage-cl-266905-model

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
