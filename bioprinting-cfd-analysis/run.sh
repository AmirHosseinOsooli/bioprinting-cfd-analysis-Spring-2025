#!/bin/bash

# Bioprinting CFD Analysis Tool - Run Script
# This script launches the Streamlit application

echo "🧬 Starting Bioprinting CFD Analysis Tool..."
echo ""

# Check if virtual environment exists and activate it
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Check if Streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit is not installed!"
    echo "Please run: ./setup.sh"
    exit 1
fi

# Launch the app
echo "Launching application..."
echo "The app will open in your default browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo "============================================"
echo ""

streamlit run app.py
