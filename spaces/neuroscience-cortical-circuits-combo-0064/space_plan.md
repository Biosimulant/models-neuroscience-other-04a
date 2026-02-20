# Space Plan - neuroscience-cortical-circuits-combo-0064

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-cerebellar-golgi-cells-dendritic-processing-and-266806-model, neuroscience-other-cerebellar-golgi-cells-dendritic-processing-synaptic-plasticity-osb266806-model, neuroscience-other-cerebellar-granular-layer-maex-and-de-schutter-1-227363-model, neuroscience-other-cerebellar-granular-layer-osb227363-model

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
