This is the README for a cerebellar Golgi cell model expanded with STDP:

> "Coincidence detection between apical and basal dendrites drives STDP in cerebellar Golgi cells"
>
> E. Pali 1, S. Masoli 1, D. Di Domenico 1, T. Sorbo 1, F. Prestori 1*, E. D'Angelo 1,2*
>
> 1 Department of Brain and Behavioural Sciences, University of Pavia, Pavia, Italy 27100
>
> 2 Digital Neuroscience Centre, IRCCS Mondino Foundation, Pavia, Italy 27100

"Cerebellar Golgi cells (GoCs), segregate parallel fiber (pf), and mossy fiber (mf) inputs on apical and basal dendrites. Computational modeling predicted that this anatomical arrangement, coupled with a specific ionic channel localization, could be instrumental to drive STDP at mf-GoC synapses. Here, we test this hypothesis with GoC patch-clamp recordings in acute mouse cerebellar slices. Repeated mf-pf pairing on the theta-band within a ± 50 ms time window induces anti-symmetric Hebbian-STDP, with spike-timing long-term potentiation or depression (st-LTP or st-LTD) occurring when action potentials (APs) elicited by pf stimulation follow or precede the activation of mf synapses, respectively. Mf-GoC STDP induction requires AP backpropagation from apical to basal dendrites, NMDA receptor activation at mf-GoC synapses, and intracellular calcium changes. Importantly, STDP is inverted by inhibitory control. Thus, experimental evidence confirms and extends model predictions suggesting that GoC STDP can bind molecular layer to granular layer activity, regulating cerebellar computation and learning."

[doi:10.1038/s42003-025-08153-1](https://doi.org/10.1038/s42003-025-08153-1)



Models built by Stefano Masoli in Python3/Neuron8. stefano.masoli@unipv.it

## Requirements:

The models was implemented in Python3 and NEURON 8

NEURON 8.2.4 runs the models without issues but the models do not run on NEURON 9, yet.

The model has similar computational requirement has the original Golgi cell model (Masoli et al,. 2020)


## Usage instructions:

Download and extract the archive.

Under Linux/Unix:

- Change directory to "`Golgi_SDTP_modeldb`" folder. 
Run `nrnivmodl ./mod_files` to compile the mod files.

- Run "`nrngui -python ./protocols/01_LTD`" or "`nrngui -python ./protocols/02_LTP`" to run the protocols.

- Run `python3 LTD_LTP_analisys.py` to plot the values obtained from the simulations.

### Attention: 
The model does not work with the variable time step!

Not tested under NEURON for windows or macOS.
