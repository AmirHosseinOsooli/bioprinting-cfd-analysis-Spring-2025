@echo off
REM Bioprinting CFD Analysis Tool - Run Script (Windows)
REM This script launches the Streamlit application

echo ============================================
echo Starting Bioprinting CFD Analysis Tool...
echo ============================================
echo.

REM Check if virtual environment exists and activate it
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Check if Streamlit is installed
streamlit --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Streamlit is not installed!
    echo Please run: setup.bat
    pause
    exit /b 1
)

REM Launch the app
echo Launching application...
echo The app will open in your default browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo ============================================
echo.

streamlit run app.py
