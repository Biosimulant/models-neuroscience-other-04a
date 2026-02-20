# Space Plan - neuroscience-cortical-circuits-combo-0066

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-cerebellar-nuclear-neuron-sudhakar-et-al-2015-185513-model, neuroscience-other-cerebellar-optokinetic-response-osb267334-model, neuroscience-other-cerebellar-parallel-fiber-purkinje-cell-ltd-ltp-osb235376-model, neuroscience-other-cerebellar-phase-locked-tacs-essential-tremor-osb266842-model

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
