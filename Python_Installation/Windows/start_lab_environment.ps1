# Set the path to include the Anaconda distribution
$CONDA_DIR="$env:USERPROFILE\anaconda3"
$env:Path="$env:Path;$CONDA_DIR\Scripts"
$env:Path="$env:Path;$CONDA_DIR\condabin"

conda activate pelagos
jupyter-lab