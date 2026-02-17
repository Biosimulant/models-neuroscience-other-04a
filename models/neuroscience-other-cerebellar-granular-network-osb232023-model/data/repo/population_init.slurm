#!/bin/sh
# Script for initializing cell populations in the SLURM system
#
# Written by Shyam Kumar Sudhakar, Ivan Raikov, Tom Close, Rodrigo Publio, Daqing Guo, and Sungho Hong
# Computational Neuroscience Unit, Okinawa Institute of Science and Technology, Japan
# Supervisor: Erik De Schutter
#
# Correspondence: Sungho Hong (shhong@oist.jp)
#
# September 16, 2017

## Some parameters for running a SLURM job
#SBATCH --tasks=10
#SBATCH --cpus-per-task=2
#SBATCH --job-name=GL_POP
#SBATCH --mem-per-cpu=20g
#SBATCH --error=population_init.err.log
#SBATCH --output=population_init.out.log

echo PYTHONPATH is $PYTHONPATH

echo "==============Starting population init==============="
cd SHAREDDIR/model

export PATH=... # Set paths for python, etc. here
NEURONHOME=... # Set your NEURONHOME here
export PATH=$NEURONHOME/nrn/x86_64/bin:$NEURONHOME/iv/x86_64/bin:$PATH
export LD_LIBRARY_PATH=$NEURONHOME/nrn/x86_64/lib:$NEURONHOME/iv/x86_64/lib:$LD_LIBRARY_PATH

NBSUBDIV=1000000000

## Initialize cell populations first
mpirun nrniv -mpi -python main.py --initpop

echo "==============Population init has ended==============="
