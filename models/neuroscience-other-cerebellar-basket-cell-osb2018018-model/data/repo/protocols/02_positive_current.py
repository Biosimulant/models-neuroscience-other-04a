from neuron import h 
from basket import Basket

import multiprocessing

cell = Basket()

stimdata = dict()
stimdata['stim0del'] = 200
stimdata['stim0dur'] = 2000
stimdata['stim0amp'] = 0.020 


stimdata['stim1del'] = 2400 
stimdata['stim1dur'] = 2000 
stimdata['stim1amp'] = 0.040 

stimdata['timeglobal'] = 4600 

fixed_time = h.CVode()
fixed_time.active(0) #0 fixed step, 1 variaeble time step


h.load_file("parcom.hoc")
p = h.ParallelComputeTool()
p.change_nthread(8,1)
p.multisplit(1)

h('load_file("vm.ses")')
h.nrncontrolmenu()

h.dt = 0.025
h.celsius = 32
h.tstop = stimdata['timeglobal']
h.v_init = -65  

stim = [h.IClamp(0.5,sec=cell.soma[0]), h.IClamp(0.5,sec=cell.soma[0])] 

stim[0].delay = stimdata['stim0del']
stim[0].dur = stimdata['stim0dur']
stim[0].amp = stimdata['stim0amp'] 

stim[1].delay = stimdata['stim1del']
stim[1].dur = stimdata['stim1dur']
stim[1].amp = stimdata['stim1amp'] 


def initialize():
    h.finitialize()
    h.run()

initialize()
  
np.savetxt('02_positive_currents.txt', np.column_stack((np.array(cell.time),np.array(cell.voltage))), delimiter = ' ')
