from neuron import h, gui
from basket import Basket

import multiprocessing

cell = Basket()

stimdata = dict()
stimdata['stim0del'] = 2000 
stimdata['stim0dur'] = 2000 
stimdata['stim0amp'] = -0.016 


stimdata['timeglobal'] = 6000

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

stim = [h.IClamp(0.5,sec=cell.soma[0])] 

stim[0].delay = stimdata['stim0del']
stim[0].dur = stimdata['stim0dur']
stim[0].amp = stimdata['stim0amp'] 


    
def initialize():
    h.finitialize()
    h.run()
    
initialize()
    

np.savetxt('03_negative_current.txt', np.column_stack((np.array(cell.time),np.array(cell.voltage))), delimiter = ' ')


