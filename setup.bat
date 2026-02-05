@echo off
REM Bioprinting CFD Analysis Tool - Setup Script (Windows)
REM This script installs all dependencies and prepares the environment

echo ============================================
echo Bioprinting CFD Analysis Tool - Setup
echo ============================================
echo.

REM Check Python version
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

python --version
echo.

REM Create virtual environment
set /p create_venv="Create virtual environment? (recommended) [Y/n]: "
if /i "%create_venv%"=="" set create_venv=Y
if /i "%create_venv%"=="Y" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Virtual environment created and activated
    echo.
)

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip --quiet

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet

if %errorlevel% equ 0 (
    echo All dependencies installed successfully
) else (
    echo Error installing dependencies
    echo Please try manually: pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo ============================================
echo Setup completed successfully!
echo ============================================
echo.
echo To start the application, run:
echo   run.bat
echo.
echo For more information, see:
echo   - README.md for full documentation
echo   - QUICKSTART.md for a 5-minute guide
echo.
pause
