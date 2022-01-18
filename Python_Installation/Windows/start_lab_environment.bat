@echo off

rem Change to home directory
cd /d %userprofile%

rem Set paths
set "CONDA_DIR=%userprofile%\anaconda3"
set "Path=%CONDA_DIR%\Scripts;%Path%"
set "Path=%CONDA_DIR%\condabin;%Path%"

CALL conda.bat activate pelagos

rem Activate environment and start Jupyter-lab
%windir%\System32\cmd.exe "/K" jupyter-lab
