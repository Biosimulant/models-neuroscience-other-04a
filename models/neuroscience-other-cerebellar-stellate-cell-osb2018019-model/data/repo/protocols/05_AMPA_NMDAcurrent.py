from neuron import h 
from stellate import Stellate
import numpy as np
import multiprocessing

cell = Stellate()

h.load_file("parcom.hoc")
p = h.ParallelComputeTool()
p.change_nthread(2,1)
p.multisplit(1)

h('load_file("vm.ses")')
h.nrncontrolmenu()

stimdata = dict()
stimdata['timeglobal'] = 8000
synapsesdata = dict()

cell.createsyn()

freq_interv = [5, 10, 20, 50, 100, 250]

for ms_step in freq_interv:
    spk_stim_mossy = []
    spk_nc_pfsyn = []
    spk_nc_pfsyn_nmda = []
    
    spk_stim = h.NetStim()
    spk_stim.interval = ms_step
    spk_stim.number = 10
    spk_stim.noise = 0
    spk_stim.start = 3000
    
    spk_stim_mossy.append(spk_stim)
    
    for m in range(int(len(spk_stim_mossy))):
        spk_nc_pfsyn.append([h.NetCon(spk_stim_mossy[m],pf_sc.input,0,0.1,1) for pf_sc in cell.pfsc])
        spk_nc_pfsyn_nmda.append([h.NetCon(spk_stim_mossy[m],pfnmda.input,0,0.1,1) for pfnmda in cell.pf_scnmda])

    fixed_time = h.CVode()
    fixed_time.active(0) 

    h.dt = 0.025
    h.celsius = 32 #37
    h.tstop = stimdata['timeglobal']
    h.v_init = -60
      

    def initialize():
        h.finitialize()
        h.run()
        
    initialize()

    np.savetxt('05_singlesynAMPA_Hz_' + str(int(1000/ms_step)) + '.txt', np.column_stack((np.array(cell.time),np.array(cell.pfsc[0].i['AMPA'][0]))), delimiter = ' ')
    np.savetxt('05_singlesynNMDA_Hz_' + str(int(1000/ms_step)) + '.txt', np.column_stack((np.array(cell.time),np.array(cell.pf_scnmda[0].i['NMDA'][0]))), delimiter = ' ')

    np.savetxt('05_voltagetraceAMPA-NMDA_Hz_' + str(int(1000/ms_step)) + '.txt', np.column_stack((np.array(cell.time),np.array(cell.voltage))), delimiter = ' ')
