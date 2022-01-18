#!/bin/bash --login

case "$OSTYPE" in
    darwin*) export CONDA_DIR=${HOME}/opt/anaconda3 ;;
    *) export CONDA_DIR=${HOME}/anaconda3 ;;
esac

export PATH=$CONDA_DIR/bin:$PATH

cd $HOME
conda init bash
source activate pelagos
conda env list
jupyter-lab
