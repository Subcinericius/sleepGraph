# Set the path to include the Anaconda distribution
$CONDA_DIR="$env:USERPROFILE\anaconda3"
$env:Path="$env:Path;$CONDA_DIR\Scripts"
$env:Path="$env:Path;$CONDA_DIR\condabin"

# Deactivate and remove the environment
Write-Output "Deactivating old environment"
conda deactivate pelagos
Write-Output "Removing old environment"
conda remove -n pelagos --all -y

# Remove env folder if it exists, yucky!
#$env_folder = "$CONDA_DIR\envs\pelagos"
#if (Test-Path -Path $env_folder) {
#    Remove-Item -path $env_folder -recurse
#    Write-Output "Removed environment directory $env_folder"
#}

Read-Host -Prompt "Press Enter to exit"