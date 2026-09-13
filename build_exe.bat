@echo off

echo ----------------------------------------------------------------------
echo Creating an EXE named RPyTkGUICreator.exe inside the ./dist folder.
echo ----------------------------------------------------------------------
echo Please wait...
echo.

setlocal

REM Get current full path (where this batch file is located), with no trailing slash
cd /d "%~dp0"
set "MY_CURRENT_DIR=%~dp0"
if "%MY_CURRENT_DIR:~-1%"=="\" set "MY_CURRENT_DIR=%MY_CURRENT_DIR:~0,-1%"
echo The current active directory is: "%CD%"

set PYTHONWARNINGS=ignore

REM Activate the virtual enviroment
echo Activating Virtual Enviroment...
call .\venv\Scripts\activate.bat
echo Virtual Enviroment Activated.

REM Create the RPyTkGUICreator.EXE - one long command line....
pyinstaller --noconfirm --onefile --windowed --version-file="file_version_info.txt" --add-data "%MY_CURRENT_DIR%\favicon.ico;." --icon=favicon.ico --add-data "%MY_CURRENT_DIR%\icons;app_files/" --add-data "%MY_CURRENT_DIR%\venv\Lib\site-packages\chlorophyll;chlorophyll/" --add-data "%MY_CURRENT_DIR%\venv\Lib\site-packages\chlorophyll\colorschemes;colorschemes/" --add-data "%MY_CURRENT_DIR%\config.txt;app_files/" --add-data "%MY_CURRENT_DIR%\theme.toml;app_files/" --add-data "%MY_CURRENT_DIR%\library.py;app_files/" --name "RPyTkGUICreator" "%MY_CURRENT_DIR%\RPyTkGUICreator.py"

REM Deactivate the virtual enviroment
echo Deactivating Virtual Enviroment...
call .\venv\Scripts\deactivate.bat
echo Virtual Enviroment Deactivated.


echo ----------------------------------------------------------------------
echo Finished Creating 'RPyTkGUICreator.exe' inside the ./dist folder.
echo ----------------------------------------------------------------------

pause

exit

