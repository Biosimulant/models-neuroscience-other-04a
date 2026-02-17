#!/bin/sh
#
# Example script to compile and deploy brep
#
# Written by Ivan Raikov and Sungho Hong
# Computational Neuroscience Unit, Okinawa Institute of Science and Technology, Japan
# Supervisor: Erik De Schutter
#
# Correspondence: Ivan Raikov (iraikov@stanford.edu)
#
# September 16, 2017

DEPLOYDIR=... # Where to install brep
CHICKENHOME=... # Where your chicken-scheme is installed
MPIHOME=... # Here specify your mpi home

mkdir -p $DEPLOYDIR

## Get bvspis.sh
curl -L -O http://www.netlib.org/toms/770.gz
gunzip 770.gz
mkdir bvspis && awk 'NR>4' 770 > bvspis/bvspis.sh && chmod u+x bvspis/bvspis.sh
rm 770
pushd bvspis && ./bvspis.sh && popd

## Install packages first
MPI_DIR=$MPIHOME $CHICKENHOME/bin/chicken-install mpi
$CHICKENHOME/bin/chicken-install matchable datatype typeclass cis kd-tree \
random-mtzig  getopt-long srfi-4-utils srfi-63 records bind srfi-42 \
srfi-4-comprehensions mathh lalr parametric-curve
BVSPIS_PATH=$PWD/bvspis $CHICKENHOME/bin/chicken-install bvsp-spline

## Install and deploy everything
MPI_DIR=$MPIHOME $CHICKENHOME/bin/chicken-install -deploy -prefix $DEPLOYDIR mpi
BVSPIS_PATH=$PWD/bvspis $CHICKENHOME/bin/chicken-install -deploy -prefix $DEPLOYDIR bvsp-spline
$CHICKENHOME/bin/chicken-install -deploy -prefix $DEPLOYDIR matchable datatype typeclass cis kd-tree \
random-mtzig  getopt-long srfi-4-utils srfi-63 records bind srfi-42 \
srfi-4-comprehensions mathh lalr parametric-curve

$CHICKENHOME/bin/csc -deploy -O3 -d0 -o $DEPLOYDIR brep.scm
