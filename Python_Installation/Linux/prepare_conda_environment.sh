#!/bin/bash --login

# Set paths
case "$OSTYPE" in
    darwin*) export CONDA_DIR=${HOME}/opt/anaconda3 ;;
    *) export CONDA_DIR=${HOME}/anaconda3 ;;
esac

export PATH=$CONDA_DIR/bin:$PATH

# Get the directory where this script lives
script_dir=$(dirname "$0")

conda create --name pelagos --file ${script_dir}/conda_packages.txt --force -q -y
conda init bash
conda activate pelagos

# Install the TOC extension
jupyter labextension install @jupyterlab/toc
jupyter lab build
