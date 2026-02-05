#!/bin/bash

# Bioprinting CFD Analysis Tool - Setup Script
# This script installs all dependencies and prepares the environment

echo "🧬 Bioprinting CFD Analysis Tool - Setup"
echo "========================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Check if Python 3.8+ is available
if ! python3 -c 'import sys; assert sys.version_info >= (3,8)' 2>/dev/null; then
    echo "❌ Error: Python 3.8 or higher is required"
    echo "Please install Python 3.8+ from https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python version is compatible"
echo ""

# Create virtual environment (optional but recommended)
read -p "Create virtual environment? (recommended) [Y/n]: " create_venv
create_venv=${create_venv:-Y}

if [[ $create_venv =~ ^[Yy]$ ]]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    
    # Activate virtual environment
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
        echo "✅ Virtual environment created and activated"
    else
        echo "⚠️  Virtual environment creation failed, continuing without it"
    fi
    echo ""
fi

# Upgrade pip
echo "Upgrading pip..."
python3 -m pip install --upgrade pip --quiet

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet

if [ $? -eq 0 ]; then
    echo "✅ All dependencies installed successfully"
else
    echo "❌ Error installing dependencies"
    echo "Please try manually: pip install -r requirements.txt"
    exit 1
fi

echo ""
echo "========================================"
echo "🎉 Setup completed successfully!"
echo "========================================"
echo ""
echo "To start the application, run:"
echo "  streamlit run app.py"
echo ""
echo "Or use the run script:"
echo "  ./run.sh"
echo ""
echo "For more information, see:"
echo "  - README.md for full documentation"
echo "  - QUICKSTART.md for a 5-minute guide"
echo ""
