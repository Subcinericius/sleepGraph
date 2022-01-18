@echo off

rem Set the path to include the Anaconda distribution
set "CONDA_DIR=%userprofile%\anaconda3"
set "Path=%CONDA_DIR%\Scripts;%Path%"
set "Path=%CONDA_DIR%\condabin;%Path%"

rem set "ENV_DIR=%CONDA_DIR%\envs\pelagos"
rem rmdir /s "%ENV_DIR"

rem Remove conda environment
CALL conda.bat deactivate
conda remove --name pelagos --all


