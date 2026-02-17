from neuron import h,gui 
from basket import Basket
import multiprocessing
import numpy as np

cell = Basket()


fixed_time = h.CVode()
fixed_time.active(0) #0 fixed step, 1 variable time step

h.load_file("parcom.hoc")
p = h.ParallelComputeTool()
p.change_nthread(8,1)
p.multisplit(1)

h.nrncontrolmenu()

stimdata = dict()

h.dt = 0.025
h.celsius = 32
h.tstop = 300
h.v_init = -65

vc = [h.SEClamp(0.5,sec=cell.soma[0])] 

dur1 = 100
amp1 = -70
vc[0].dur1 = dur1
vc[0].amp1 = amp1

dur2 = 100
amp2 = -80
vc[0].dur2 = dur2
vc[0].amp2 = amp2

dur3 = 100
amp3 = -70
vc[0].dur3 = dur3
vc[0].amp3 = amp3


vc[0].rs = 3

vc_current = h.Vector()
vc_current.record(vc[0]._ref_i)
    

def initialize():
    h.finitialize()
    h.run()
    
initialize()

#Equation for the resistance.
import math

new_RIN = vc_current[4000] - vc_current[8000]
ra = 10/math.fabs(np.array(new_RIN))
print('ra Megaohm', ra)  

fo = open('04_trace_indiv_iVC_value.csv', "w")
fo.write(str(ra))
fo.close()                 

quit()
