#!/bin/sh
# Script for compute the parallel fiber-Golgi cell connectivity in the SLURM system
#
# Written by Shyam Kumar Sudhakar, Ivan Raikov, Tom Close, Rodrigo Publio, Daqing Guo, and Sungho Hong
# Computational Neuroscience Unit, Okinawa Institute of Science and Technology, Japan
# Supervisor: Erik De Schutter
#
# Correspondence: Sungho Hong (shhong@oist.jp)
#
# September 16, 2017

## Some parameters for running a SLURM job
#SBATCH --job-name=GL_BREP
#SBATCH --mem-per-cpu=5G
#SBATCH --ntasks=120
#SBATCH	--cpus-per-task=2
#SBATCH --input=none
## Standard output and standard error files
#SBATCH --output=SHAREDDIR/pf_goc_projection.out.log
#SBATCH --error=SHAREDDIR/pf_goc_projection.err.log


echo "==============Starting run==============="

cd SHAREDDIR/model

## Random seed to be used by BREP
RNG_SEEDS="73,79,83,89,97,101,103,107,109,113"

## Recheck which PARAMDIR we are using
echo $PARAMDIR

BREP=... # Set your path to brep executable here

mpirun $BREP --rng-seeds="$RNG_SEEDS"  --gc-points=GCcoordinates.dat --gct-points=GCTcoordinates.dat --goc-points=GoCcoordinates.dat --config-file=$PARAMDIR/Parameters.hoc -:hm16000M

echo "==============run has ended==============="

## Copy and clean up the connectivity data
cat GoCtoGoCsources[0-9]*.dat > GoCtoGoCsources.dat
cat GoCtoGoCtargets[0-9]*.dat > GoCtoGoCtargets.dat
cat GoCtoGoCdistances[0-9]*.dat > GoCtoGoCdistances.dat

cat GoCtoGoCgapsources[0-9]*.dat > GoCtoGoCgapsources.dat
cat GoCtoGoCgaptargets[0-9]*.dat > GoCtoGoCgaptargets.dat
cat GoCtoGoCgapdistances[0-9]*.dat > GoCtoGoCgapdistances.dat

rm GoCtoGoCsources[0-9]*.dat GoCtoGoCtargets[0-9]*.dat GoCtoGoCdistances[0-9]*.dat
rm GoCtoGoCgapsources[0-9]*.dat GoCtoGoCgaptargets[0-9]*.dat GoCtoGoCgapdistances[0-9]*.dat
