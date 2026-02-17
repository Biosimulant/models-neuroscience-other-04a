import neuron
from neuron import h
import time
import numpy
from numpy import genfromtxt
import csv

start_time = time.time()

openfile2='MC_voltage.hoc'
filename2='Fig4Bii_1.csv'
filename3='Fig4Bii_2.csv'
filename4='Fig4Bii_3.csv'

#trial 1
h('ginputmono=0.003375')
h('ginputpoly=0.001875')
h('latepolyinput=0.064072266')

#define parameters
h('tau1inputmono=1.4')
h('tau2inputmono=1.6')
h('tau1inputpoly=5')
h('tau2inputpoly=347.4')
h('membres=0.000362')
h('restV=-54')
h('syn1onset=202')
h('syn2onset=202')
h('syn3onset=202')

h.xopen(openfile2)

csv.writer(open(filename2,'w',newline='')).writerows(zip(h.volt2))

#trial 2
h('ginputmono=0.003375')
h('ginputpoly=0.00125')
h('latepolyinput=0.064072266')

h.xopen(openfile2)

csv.writer(open(filename3,'w',newline='')).writerows(zip(h.volt2))

#trial 3
h('ginputmono=0.00253125')
h('ginputpoly=0.001875')
h('latepolyinput=0.056953125')


h.xopen(openfile2)

csv.writer(open(filename4,'w',newline='')).writerows(zip(h.volt2))


total_time = (time.time() - start_time)
print('Total time to run ' + str(total_time) + ' seconds')



