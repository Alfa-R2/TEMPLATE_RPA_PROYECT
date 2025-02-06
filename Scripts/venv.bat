@echo off

rem ----------------------------------------------------------------------------
rem Developer Setup Script: 
rem This is an automation script to assist with setting up a Python virtual 
rem environment and installing the project in editable mode mode.

rem Steps executed by this script:
rem 1. Creates a virtual environment named '.venv' using the command:
rem    py -m venv .venv
rem    - This command creates a self-contained Python environment in the current 
rem      directory. It isolates the project’s dependencies from the global Python 
rem      environment.

rem 2. Activates the virtual environment using:
rem    .\.venv\Scripts\activate
rem    - This command activates the virtual environment, allowing you to use the 
rem      Python interpreter and libraries from within this isolated environment.

rem ----------------------------------------------------------------------------

rem Show title
echo Developer Setup Script: 
echo.

rem Change directory from scripts to its parent directory (project root)
echo Current directory: %cd%
cd ..
echo Changed to: %cd%
echo.

rem Create a virtual environment in the root folder
if not exist .venv (
    py -m venv .venv
    echo Virtual environment created.
)

rem Activate the virtual environment
call .\.venv\Scripts\activate
echo Virtual environment activated.
echo.

rem Upgrade pip within the virtual environment
py -m pip install --upgrade pip
echo.

