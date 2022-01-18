@echo off

rem rem comments out the line!

rem Set the path to include the Anaconda distribution
set "CONDA_DIR=%userprofile%\anaconda3"
set "Path=%CONDA_DIR%\Scripts;%Path%"
set "Path=%CONDA_DIR%\condabin;%Path%"

set "manifest=%~dp0conda_packages.txt"

conda create --name pelagos --file "%manifest%" --force -q -y
CALL conda.bat activate pelagos

jupyter labextension install @jupyterlab/toc
jupyter lab build

%windir%\System32\cmd.exe "/K" activate pelagos