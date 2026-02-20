# Space Plan - neuroscience-general-combo-0039

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-ca2-current-versus-ca2-channel-cooperativity-exocytosis-osb125676-model, neuroscience-other-ca2-current-versus-ca2-channel-cooperativity-of-125676-model, neuroscience-other-ca2-oscillations-in-single-astrocytes-lavrentovi-223144-model

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
