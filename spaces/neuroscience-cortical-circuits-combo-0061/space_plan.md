# Space Plan - neuroscience-cortical-circuits-combo-0061

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-cell-models-wiring-variations-that-enable-constrain-neural-computation-sensory-osbTobinEtAl2017-model, neuroscience-other-cell-type-specific-integration-feedforward-feedback-synaptic-inputs-osb267509-model, neuroscience-other-cellular-classes-revealed-heartbeat-related-modulation-extracellular-aps-osb263961-model, neuroscience-other-cellular-function-given-parametric-variation-hh-excitability-osb262464-model

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
