# Set the path to include the Anaconda distribution
$CONDA_DIR="$env:USERPROFILE\anaconda3"
$env:Path="$env:Path;$CONDA_DIR\Scripts"
$env:Path="$env:Path;$CONDA_DIR\condabin"

# Function to get the script root
Function Get-PSScriptRoot
{
    $ScriptRoot = ""

    Try
    {
        $ScriptRoot = Get-Variable -Name PSScriptRoot -ValueOnly -ErrorAction Stop
    }
    Catch
    {
        $ScriptRoot = Split-Path $script:MyInvocation.MyCommand.Path
    }

    Write-Output $ScriptRoot
}

# Get the directory where this script is located and the manifest file
$scriptdir=Get-PSScriptRoot
$manifest="$scriptdir\conda_packages.txt"
Write-Output "Manifest to read is is $manifest"

# Now create the environment
conda create --name pelagos --file "$manifest" --force -y --quiet

# Activate the environment
conda activate pelagos
jupyter labextension install @jupyterlab/toc
jupyter lab build

Read-Host -Prompt "Press Enter to exit"