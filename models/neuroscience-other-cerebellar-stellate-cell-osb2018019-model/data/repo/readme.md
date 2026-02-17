# README: Stellate Cell Model

This is the README for the stellate cell model for the paper:

**Stellate cell computational modeling predicts signal filtering in the molecular layer circuit of cerebellum**

Martina Francesca Rizza, Francesca Locatelli, Stefano Masoli, Diana Sánchez‑Ponce, Alberto Muñoz, Francesca Prestori* and Egidio D’Angelo*

---

The functional properties of cerebellar stellate cells and the way they regulate molecular layer activity are still unclear.
We have measured stellate cells electroresponsiveness and their activation by parallel fiber bursts.
Stellate cells showed intrinsic pacemaking, along with characteristic responses to depolarization and hyperpolarization,
and showed a marked short‑term facilitation during repetitive parallel fiber transmission. Spikes were emitted after a
lag and only at high frequency, making stellate cells operate as delay‑high‑pass filters. A detailed computational model
summarizing these physiological properties allowed exploration of different functional configurations of the parallel
fiber—stellate cell—Purkinje cell circuit. Simulations showed that, following parallel fiber stimulation, Purkinje cells
almost linearly increased their response with input frequency, but such an increase was inhibited by stellate cells,
which leveled the Purkinje cell gain curve to its 4 Hz value. When reciprocal inhibitory connections between stellate
cells were activated, the control of stellate cells over Purkinje cell discharge was maintained only at very high frequencies.
These simulations thus predict a new role for stellate cells, which could endow the molecular layer with low‑pass and band‑pass
filtering properties regulating Purkinje cell gain and, along with this, also burst delay and the burst‑pause responses pattern.

---

## Models

Built by Martina Francesca Rizza in Python3/NEURON 8.

---

## Requirements

- Implemented in Python3 and NEURON 8
- NEURON 8.2.4 runs the models without issues
    (Models do **not** run on NEURON 9 yet)
- Uses NEURON multisplit to distribute calculation on 2 cores

---

## Usage Instructions

1. Download and extract the archive.
2. Under Linux/Unix:

    - Change directory to `CB_stellate_cell_model` folder.
    - Run `nrnivmodl ./mod_files` to compile the mod files.
    - Run `nrngui -python ./protocols/0x_protocol`
        (replace `0x_protocol` with the name of the Python file in the protocols directory)

---

## Provided Protocols

The model is provided with five premade protocols able to reproduce:

**01** - Spontaneous firing  
**02** - Positive current injections  
**03** - Negative current injection  
**04** - Input resistance  
**05** - Synaptic activity and current recordings

---

## Attention

- The model does **not** work with the variable time step!
- Not tested under NEURON for Windows or Mac OS.
