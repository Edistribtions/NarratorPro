@echo off
echo ==========================================
echo Creating NarratorPro Project Structure...
echo ==========================================

REM Ensure we're in the directory containing this BAT file
cd /d "%~dp0"

REM Create directories
mkdir src\narratorpro\application 2>nul
mkdir src\narratorpro\config 2>nul
mkdir src\narratorpro\core 2>nul
mkdir src\narratorpro\gui 2>nul
mkdir src\narratorpro\resources 2>nul
mkdir src\narratorpro\services 2>nul
mkdir src\narratorpro\utils 2>nul

REM Root package files
type nul > src\narratorpro\__init__.py
type nul > src\narratorpro\__main__.py
type nul > src\narratorpro\app.py
type nul > src\narratorpro\version.py

REM application
type nul > src\narratorpro\application\__init__.py
type nul > src\narratorpro\application\application.py

REM config
type nul > src\narratorpro\config\__init__.py
type nul > src\narratorpro\config\settings.py

REM core
type nul > src\narratorpro\core\__init__.py
type nul > src\narratorpro\core\logger.py
type nul > src\narratorpro\core\paths.py

REM gui
type nul > src\narratorpro\gui\__init__.py
type nul > src\narratorpro\gui\main_window.py
type nul > src\narratorpro\gui\menu_bar.py
type nul > src\narratorpro\gui\status_bar.py
type nul > src\narratorpro\gui\tool_bar.py
type nul > src\narratorpro\gui\splash.py

REM resources
type nul > src\narratorpro\resources\__init__.py

REM services
type nul > src\narratorpro\services\__init__.py

REM utils
type nul > src\narratorpro\utils\__init__.py

echo.
echo ==========================================
echo Project structure created successfully.
echo ==========================================
pause