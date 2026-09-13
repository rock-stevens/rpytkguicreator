@echo off

echo -----------------------------
echo Running RPyTkGUICreator
echo -----------------------------
echo.

setlocal

REM Get current full path (where this batch file is located), with no trailing slash
cd /d "%~dp0"
set "MY_CURRENT_DIR=%~dp0"
if "%MY_CURRENT_DIR:~-1%"=="\" set "MY_CURRENT_DIR=%MY_CURRENT_DIR:~0,-1%"
echo The current active directory is: "%CD%"

set PYTHONWARNINGS=ignore


echo Starting RPyTkGUICreator...

REM check if python can be found...
REM old school, i don't use powershell.
REM i didn't use 'command' && ( ok ) || ( err exit ) way of error checking
REM up to the user anyway to ensure Python 3.10.8 or higher is installed
call python --version > nul 2>&1
if %errorlevel% equ 0 (
    echo Found Python :OK
) else (
    echo Error: NO Python found installed on your system, or it is not in your path. It is needed in order to install RPyTkGUICreator.
    echo Ensure Python 3.10.8 or higher is installed on your system, AND also in your PATH.
    echo If NOT installed, Install Python 3.10.8 or higher, make sure you check the PATH box at end of the installation process. 
	echo Python 3.10.8 or higher is needed in order to install RPyTkGUICreator.
    pause
    exit /b 1
)



REM just display the python version, that's all
for /f "tokens=2" %%I in ('python --version 2^>^&1') do (
    echo Python Version : %%I
)



echo Activating Virtual Enviroment for RPyTkGUICreator...
call .\venv\Scripts\activate.bat
echo RPyTkGUICreator Virtual Enviroment Activated.


echo Launching RPyTkGUICreator...
python RPyTkGUICreator.py

echo Deactivating Virtual Enviroment for RPyTkGUICreator...
call .\venv\Scripts\deactivate.bat
echo RPyTkGUICreator Virtual Enviroment Deactivated.

echo Thanks for using RPyTkGUICreator.

REM wait for user to see what happened, error or not
pause

