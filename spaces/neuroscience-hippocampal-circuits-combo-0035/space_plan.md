# Space Plan - neuroscience-hippocampal-circuits-combo-0035

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-ca3-radiatum-lacunosum-moleculare-interneuron-ih-osb140732-model, neuroscience-other-calcium-waves-and-mglur-dependent-synaptic-plast-150551-model, neuroscience-other-calcium-waves-mglur-dependent-synaptic-plasticity-ca1-pyr-osb150551-model

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
