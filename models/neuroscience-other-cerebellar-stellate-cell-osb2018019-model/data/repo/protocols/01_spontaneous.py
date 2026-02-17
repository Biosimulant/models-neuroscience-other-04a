from neuron import h, gui
from stellate import Stellate

import multiprocessing

cell = Stellate()

h.load_file("parcom.hoc")
p = h.ParallelComputeTool()
p.change_nthread(2,1)
p.multisplit(1)

stimdata = dict()
stimdata['stim0del'] = 0
stimdata['stim0dur'] = 0
stimdata['stim0amp'] = 0

stimdata['timeglobal'] = 5000

fixed_time = h.CVode()
fixed_time.active(0) #0 fixed step, 1 variable time step

h('load_file("vm.ses")')
h.nrncontrolmenu()

h.dt = 0.025
h.celsius = 32
h.tstop = stimdata['timeglobal']
h.v_init = -65

    
def initialize():
    h.finitialize()
    h.run()
    

initialize()

np.savetxt('01_spontaneuos.txt', np.column_stack((np.array(cell.time),np.array(cell.voltage))), delimiter = ' ')    

quit()


