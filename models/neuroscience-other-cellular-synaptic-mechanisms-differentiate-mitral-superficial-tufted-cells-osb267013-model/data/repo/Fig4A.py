import neuron
from neuron import h
import time
import numpy
from numpy import genfromtxt
import csv

start_time = time.time()

openfile='MC_Fig4A_current.hoc'
openfile2='MC_Fig4A_voltage.hoc'
filename='Fig4Aii_current.csv'
filename2='Fig4Av_voltage.csv'

#define input data
fileinput='Fig4A_data.dat'

#define parameters
h('ginputmono=0.001')
h('tau1inputmono=.9')
h('tau2inputmono=3')
h('ginputpoly=0.001')
h('tau1inputpoly=6')
h('tau2inputpoly=131.261')
h('latepolyinput=0.001')
h('membres=0.00029')
#h('membres=0.000323')
h('restV=-54')
h('syn1onset=201')
h('syn2onset=202')
h('syn3onset=201')
polypoint=8801
datapolypoint=200
latepolypoint=40000
datalatepolypoint=8001

h.xopen(openfile)
csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
data=genfromtxt(fileinput, delimiter=',')
datamono=min(data[15:10000])
datapoly=data[datapolypoint]
datalatepoly=data[datalatepolypoint]
current=genfromtxt(filename,delimiter=',')
current=current*1000
mono=min(current[8000:8600])-current[2001]
poly=current[polypoint]-current[2001]
latepoly=current[latepolypoint]-current[2001]
print('mono='+str(mono))
print('poly='+str(poly))
print('latepoly='+str(latepoly))
print('datamono='+str(datamono))
print('datapoly='+str(datapoly))
print('datalatepoly='+str(datalatepoly))


for i in range(1,1000):

    if abs(latepoly)>abs((1.1*datalatepoly)):
        h('latepolyinput=latepolyinput*.5')
        print('if statement late poly too big')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))

    elif abs(latepoly)<abs((0.9*datalatepoly)):
        h('latepolyinput=latepolyinput*1.5')
        print('if statement late poly too small')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))

if abs(latepoly)>(.9*abs(datalatepoly)) and abs(latepoly) <(1.1*abs(datalatepoly)):
    print('no error late poly')



for i in range(1,1000):

    if abs(poly)>abs((1.1*datapoly)):
        h('ginputpoly=ginputpoly*.5')
        print('if statement poly too big')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))

    elif abs(poly)<abs((0.9*datapoly)):
        h('ginputpoly=ginputpoly*1.5')
        print('if statement poly too small')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))

if poly>(.9*datapoly) and poly <(1.1*datapoly):
    print('no error poly')


for i in range(1,1000):
    
    if abs(latepoly)>abs((1.1*datalatepoly)):
        h('latepolyinput=latepolyinput*.5')
        print('if statement late poly too big')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))
    
    elif abs(latepoly)<abs((0.9*datalatepoly)):
        h('latepolyinput=latepolyinput*1.5')
        print('if statement late poly too small')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))

for i in range(1,1000):
    
    if abs(poly)>abs((1.1*datapoly)):
        h('ginputpoly=ginputpoly*.5')
        print('if statement poly too big')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))
    
    elif abs(poly)<abs((0.9*datapoly)):
        h('ginputpoly=ginputpoly*1.5')
        print('if statement poly too small')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))

if poly>(.9*datapoly) and poly <(1.1*datapoly):
    print('no error poly')

for i in range(1,1000):
    
    if abs(mono)>abs((1.1*datamono)):
        h('ginputmono=ginputmono*.5')
        print('if statement mono too big')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))
    
    elif abs(mono)<abs((0.9*datamono)):
        h('ginputmono=ginputmono*1.5')
        print('if statement mono too small')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))


for i in range(1,1000):
    
    if abs(poly)>abs((1.1*datapoly)):
        h('ginputpoly=ginputpoly*.5')
        print('if statement poly too big')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))
    
    elif abs(poly)<abs((0.9*datapoly)):
        h('ginputpoly=ginputpoly*1.5')
        print('if statement poly too small')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))

if poly>(.9*datapoly) and poly <(1.1*datapoly):
    print('no error poly')

for i in range(1,1000):
    
    if abs(mono)>abs((1.1*datamono)):
        h('ginputmono=ginputmono*.5')
        print('if statement mono too big')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))
    
    elif abs(mono)<abs((0.9*datamono)):
        h('ginputmono=ginputmono*1.5')
        print('if statement mono too small')
        h.xopen(openfile)
        csv.writer(open(filename,'w',newline='')).writerows(zip(h.curr1))
        current=genfromtxt(filename,delimiter=',')
        current=current*1000
        mono=min(current[8000:8600])-current[2001]
        poly=current[polypoint]-current[2001]
        latepoly=current[latepolypoint]-current[2001]
        print('mono='+str(mono))
        print('poly='+str(poly))
        print('latepoly='+str(latepoly))
        print('datamono='+str(datamono))
        print('datapoly='+str(datapoly))
        print('datalatepoly='+str(datalatepoly))



if mono>(.9*datamono) and mono <(1.1*datamono):
    print('no mono error final')
if poly>(.9*datapoly) and poly <(1.1*datapoly):
    print('no poly error final')
if latepoly>(.9*datalatepoly) and latepoly <(1.1*datalatepoly):
    print('no late poly error final')


h.xopen(openfile2)

csv.writer(open(filename2,'w',newline='')).writerows(zip(h.volt2))

total_time = (time.time() - start_time)
print('Total time to run ' + str(total_time) + ' seconds')



