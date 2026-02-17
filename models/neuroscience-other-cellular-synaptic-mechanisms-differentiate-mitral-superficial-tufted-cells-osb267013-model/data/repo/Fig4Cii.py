import neuron
from neuron import h
import time
import numpy
from numpy import genfromtxt
import csv

start_time = time.time()
openfile2='sTC_voltage.hoc'
filename='testcurrent.csv'
filename2='Fig4Cii_1.csv'
filename3='Fig4Cii_2.csv'
filename4='Fig4Cii_3.csv'

#define parameters

h('ginputmono=0.017085938')
h('ginputpoly=0.003375')
h('latepolyinput=0.0014238281')



h('tau1inputmono=1.')
h('tau2inputmono=1.1')
h('tau1inputpoly=64.5')
h('tau2inputpoly=239.2')
h('membres=0.000269')
h('restV=-56')
h('syn1onset=202')
h('syn2onset=202')
h('syn3onset=202')
h.xopen(openfile2)


csv.writer(open(filename2,'w',newline='')).writerows(zip(h.volt2))


h('ginputmono=0.017085938')
h('ginputpoly=0.00253125')
h('latepolyinput=0.02162439')

h.xopen(openfile2)
csv.writer(open(filename3,'w',newline='')).writerows(zip(h.volt2))



h('ginputmono=0.017085938')
h('ginputpoly=0.00225')
h('latepolyinput=0.02883252')

h.xopen(openfile2)
csv.writer(open(filename4,'w',newline='')).writerows(zip(h.volt2))

total_time = (time.time() - start_time)
print('Total time to run ' + str(total_time) + ' seconds')



