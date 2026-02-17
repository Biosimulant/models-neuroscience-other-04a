#!/bin/bash
#
# Example job submission script for the SLURM system
#
# Usage:
#   ./batch_slurm_start.sh <name of the parameter directory under params/>
#
# Written by Shyam Kumar Sudhakar, Ivan Raikov, Tom Close, Rodrigo Publio, Daqing Guo, and Sungho Hong
# Computational Neuroscience Unit, Okinawa Institute of Science and Technology, Japan
# Supervisor: Erik De Schutter
#
# Correspondence: Sungho Hong (shhong@oist.jp)
#
# September 16, 2017
#

## Copy all the model files first to a temporary directory where the simulation will run
TIMESTAMP=`date +%a%d%b%Y_%H%M`
tmpSharedDir=$HOME/work/tmp/Molecular_Layer.${TIMESTAMP}
echo "Creating $tmpSharedDir"
mkdir -p ${tmpSharedDir}

mkdir ${tmpSharedDir}/model
echo cp -PR *.hoc *.ses *.py *.slurm populations templates mechanisms params ${tmpSharedDir}/model
cp -PR *.hoc *.ses *.py *.sh *.slurm populations templates mechanisms params ${tmpSharedDir}/model

## Check if the parameter directory is given
TESTSETDIR=${tmpSharedDir}/model/params
export PARAMDIR=${TESTSETDIR}"/"$1
echo $PARAMDIR
ls $PARAMDIR

if test "${PARAMDIR}" = ""; then
   echo "You must set PARAMDIR environment variable to point to a directory containing Parameters.hoc"
   exit 1
fi

## Compile *.mod files
olddir=$PWD

cd ${tmpSharedDir}/model
export PATH=... # Set paths for python, etc. here
NEURONHOME=... # Set your NEURONHOME here
export PATH=$NEURONHOME/nrn/x86_64/bin:$NEURONHOME/iv/x86_64/bin:$PATH
export LD_LIBRARY_PATH=$NEURONHOME/nrn/x86_64/lib:$NEURONHOME/iv/x86_64/lib:$LD_LIBRARY_PATH
PYTHONPATH=`pwd`/model:$PYTHONPATH
export PYTHONPATH

nrniv -python main.py --build

cd $olddir

## Change simulation scripts accordingly and copy them to a temporary directory
sed s#SHAREDDIR#${tmpSharedDir}#g population_init.slurm >${tmpSharedDir}/population_init.slurm
sed s#SHAREDDIR#${tmpSharedDir}#g pf_goc_projection.slurm >${tmpSharedDir}/pf_goc_projection.slurm
sed s#SHAREDDIR#${tmpSharedDir}#g simulation_job.slurm >${tmpSharedDir}/simulation_job.slurm

## Run everything
cd $tmpSharedDir
IDPOP=$(sbatch population_init.slurm)
IDPF=$(sbatch --dependency=afterok:${IDPOP##* } pf_goc_projection.slurm)
IDSIM=$(sbatch --dependency=afterok:${IDPF##* } simulation_job.slurm)

