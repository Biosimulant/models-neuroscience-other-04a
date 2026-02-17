import neuron
from neuron import h
import time
import numpy
from numpy import genfromtxt
import csv

start_time = time.time()
openfile = 'sTC_voltage.hoc'
filename='testspikes.csv'

#define parameters
h('ginputmono=0.00225')
h('ginputpoly=0.00046875')
h('latepolyinput=0.028476563')
h('tau1inputmono=.9')
h('tau2inputmono=7.2')
h('tau1inputpoly=6.2')
h('tau2inputpoly=28.5')
h('membres=0.000108')
h('restV=-56')
h('syn1onset=202')
h('syn2onset=202')
h('syn3onset=202')

h.xopen(openfile)

csv.writer(open(filename,'w',newline='')).writerows(zip(h.volt2))

total_time = (time.time() - start_time)
print('Total time to run ' + str(total_time) + ' seconds')



