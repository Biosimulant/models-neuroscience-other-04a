from neuron import h 
from basket import Basket
import numpy as np
import multiprocessing

basketcell = Basket()

cpu = multiprocessing.cpu_count()
h.load_file("parcom.hoc")
p = h.ParallelComputeTool()
p.change_nthread(8,1)
p.multisplit(1)

h('load_file("vm.ses")')
h.nrncontrolmenu()

stimdata = dict()
stimdata['timeglobal'] = 8000
synapsesdata = dict()

freq_interv = [5, 10, 20, 50, 100, 250]

basketcell.createsyn(30)

for ms_step in freq_interv:
    spk_stim_pf = []
    spk_nc_pfsynpf = []
    spk_nc_pfsynpfnmda = []

    spk_stim = h.NetStim()
    spk_stim.interval = ms_step
    spk_stim.number = 10
    spk_stim.noise = 0
    spk_stim.start = 3000

    spk_stim_pf.append(spk_stim)

    for m in range(int(len(spk_stim_pf))):
        spk_nc_pfsynpf.append([h.NetCon(spk_stim_pf[m],pf.input,0,0.1,1) for pf in basketcell.pf_bc])
        spk_nc_pfsynpfnmda.append([h.NetCon(spk_stim_pf[m],pfnmda.input,0,0.1,1) for pfnmda in basketcell.pf_bcnmda])

    fixed_time = h.CVode()
    fixed_time.active(0)

    h.dt = 0.025
    h.celsius = 32
    h.tstop = stimdata['timeglobal']
    h.v_init = -60
      
    def initialize():
        h.finitialize()
        h.run()
        
    initialize()

    np.savetxt('05_singlesynAMPA_Hz_' + str(int(1000/synapsesdata['synpfinterval'])) + '.txt', np.column_stack((np.array(basketcell.time),np.array(basketcell.pf_bc[0].i['AMPA'][0]))), delimiter = ' ')
    np.savetxt('05_singlesynNMDA_Hz_' + str(int(1000/synapsesdata['synpfinterval'])) + '.txt', np.column_stack((np.array(basketcell.time), np.array(basketcell.pf_bcnmda[0].i['NMDA'][0]))), delimiter = ' ')

    np.savetxt('05_voltagetraceAMPA-NMDA_Hz_' + str(int(1000/synapsesdata['synpfinterval'])) + '.txt', np.column_stack((np.array(basketcell.time),np.array(basketcell.voltage))), delimiter = ' ')
