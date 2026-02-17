from neuron import h 
from basket import Basket


import multiprocessing

cell = Basket()

stimdata = dict()
stimdata['timeglobal'] = 10000

fixed_step = h.CVode()
fixed_step.active(0) 


cpu = multiprocessing.cpu_count()
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

def initialize():
    h.finitialize()
    h.run()
    
initialize()
    




