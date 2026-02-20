# Space Plan - neuroscience-cortical-circuits-combo-0063

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-cerebellar-cortex-oscil-robustness-from-golgi-ce-139656-model, neuroscience-other-cerebellar-golgi-cell-model-with-stdp-pali-et-al-2017007-model, neuroscience-other-cerebellar-golgi-cell-solinas-et-al-2007a-2007b-112685-model, neuroscience-other-cerebellar-golgi-cell-stdp-osb2017007-model

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
