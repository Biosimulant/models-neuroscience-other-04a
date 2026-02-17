# README: Basket Cell Model

This is the README for the Basket cell model for the submitted paper:

**Cerebellar basket cell filtering of Purkinje cell responses elicited by low-frequency parallel fibres transmission**

Stefano Masoli*, Martina Francesca Rizza*, Teresa Soda*, Diana Sánchez-Ponce, Alberto Munoz, Francesca Prestori*, Egidio D’Angelo*

Basket cells (BC) are inhibitory interneurons of the cerebellar molecular layer (ML) forming peri-somatic synapses on Purkinje cells (PC). 
BC physiological and computational properties remained poorly understood and not clearly differentiated from those of stellate cells (SC). 
We identified BCs in acute mouse cerebellar slices and measured their intrinsic excitability and synaptic responsiveness. 
BCs and SCs were similar in some respects, although BCs showed stronger and faster synaptic excitation in response to parallel fibre (pf) bursts. 
The analysis of BC inhibition of PCs was extended over a broad parameter space using accurate multi-compartmental computational models. 
During pf bursts, the BC reduced the PC response at low-frequency, while SCs did it at high-frequency. 
BC filtering was explained by the engagement of HCN1 channels, which activated slowly during low-frequency BC-PC GABAergic transmission. 
The increase of input conductance caused by HCN1 channels in the PC soma, by shunting excitatory currents elicited by pfs and travelling toward the axon initial segment (AIS), reduced the PC output frequency. 
These simulations predict that BC and SC operate in tandem, setting the frequency band of PC transmission through the regulation of PC frequency/response curves.

---

## Models

Built by Stefano Masoli and Martina Rizza in Python3/NEURON 8.

### Requirements

- Implemented in Python3 and NEURON 8
- NEURON 8.2.4 runs the models without issues, but the models do not run on NEURON 9 yet.
- The model uses NEURON multisplit to distribute automatically the calculation on 2 cores. It can be changed but the model does not scale.

---

## Usage Instructions

1. Download and extract the archive.

2. **Under Linux/Unix:**
    - Change directory to `CB_basket_cell_model` folder.
    - Run `nrnivmodl ./mod_files` to compile the mod files.
    - Run `nrngui -python ./protocols/0x_protocol` with `0x_protocol` the name of the Python file in the `protocols` directory.

---

## Provided Protocols

The model is provided with five premade protocols able to reproduce:

**01** - Spontaneous firing  
**02** - Positive current injections  
**03** - Negative current injection  
**04** - Input resistance  
**05** - Synaptic activity and current recordings

---

**Attention:**  

- The model does **not** work with the variable time step!
- Not tested under NEURON for Windows or macOS.
