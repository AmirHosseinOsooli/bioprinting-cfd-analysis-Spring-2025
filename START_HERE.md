# 🚀 START HERE - Bioprinting CFD Analysis Tool

**Welcome!** This guide will help you get the application running in just a few steps.

## 🌐 Two Ways to Use This Tool

### Option 1: Use the Live Web App (No Installation!)

**Fastest way - just click and use:**
1. Visit: `https://YOUR-APP-URL.streamlit.app`
2. Start analyzing immediately!
3. No installation, no setup, no hassle

> **To deploy your own live version:** See [DEPLOYMENT.md](DEPLOYMENT.md)

### Option 2: Run Locally on Your Computer

**Full control, works offline:**
- Follow the instructions below
- Run on your own machine
- Customize the code

---

## 📦 What You Have

This repository contains a **ready-to-use** interactive CFD analysis tool for bioprinting. Everything you need is included!

## ⚡ Quick Start (Choose Your Platform)

### 🐧 Linux / macOS

**Option 1: Automatic Setup (Recommended)**
```bash
./setup.sh    # Install dependencies
./run.sh      # Start the app
```

**Option 2: Manual Setup**
```bash
pip install -r requirements.txt
streamlit run app.py
```

### 🪟 Windows

**Option 1: Automatic Setup (Recommended)**
```cmd
setup.bat    # Install dependencies
run.bat      # Start the app
```

**Option 2: Manual Setup**
```cmd
pip install -r requirements.txt
streamlit run app.py
```

## 🎯 What Happens Next?

1. **Setup script runs** (first time only):
   - Checks Python version (needs 3.8+)
   - Creates virtual environment (optional)
   - Installs all required packages

2. **App launches**:
   - Streamlit server starts
   - Browser opens automatically at `http://localhost:8501`
   - You see the interactive interface!

3. **Start analyzing**:
   - Default bioink (AMA) is pre-loaded
   - Adjust parameters in the sidebar
   - See results update in real-time

## 📂 Repository Structure

```
bioprinting-cfd-analysis/
├── app.py                      # 👈 Main application (run this!)
├── setup.sh / setup.bat        # 👈 One-time setup
├── run.sh / run.bat           # 👈 Quick launch
├── requirements.txt            # Python dependencies
├── README.md                   # Full documentation
├── QUICKSTART.md              # 5-minute tutorial
├── LICENSE                     # MIT License
├── .gitignore                 # Git exclusions
├── .streamlit/
│   └── config.toml            # App configuration
├── examples/
│   └── bioink_parameters.txt  # Example bioink properties
└── docs/
    └── *.png                   # Result visualizations
```

## 🔧 System Requirements

### Minimum Requirements
- **Python**: 3.8 or higher
- **RAM**: 2 GB
- **Disk Space**: 500 MB
- **OS**: Windows 10+, macOS 10.14+, or Linux

### Recommended Requirements
- **Python**: 3.10 or higher
- **RAM**: 4 GB
- **Modern web browser**: Chrome, Firefox, or Edge

## 📚 Next Steps

### First-Time Users
1. ✅ Run `setup.sh` (Linux/Mac) or `setup.bat` (Windows)
2. ✅ Run `run.sh` (Linux/Mac) or `run.bat` (Windows)
3. ✅ Read [QUICKSTART.md](QUICKSTART.md) for a 5-minute tutorial

### Experienced Users
1. ✅ Install dependencies: `pip install -r requirements.txt`
2. ✅ Run app: `streamlit run app.py`
3. ✅ Read [README.md](README.md) for detailed documentation

### Researchers & Developers
1. ✅ Read [README.md](README.md) for complete documentation
2. ✅ Check `examples/` for bioink parameters
3. ✅ Modify `app.py` to customize calculations

## 🐛 Troubleshooting

### Problem: "Python not found"
**Solution:**
- Install Python from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation
- Restart your terminal/command prompt

### Problem: "Streamlit not found" after setup
**Solution:**
```bash
pip install streamlit --upgrade
```

### Problem: "Module not found" errors
**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Problem: Browser doesn't open automatically
**Solution:**
- Open manually: `http://localhost:8501`
- Check if port 8501 is available
- Try a different browser

### Problem: App runs but plots don't show
**Solution:**
- Refresh the browser (F5)
- Clear browser cache
- Update packages: `pip install -r requirements.txt --upgrade`

## 🎓 Learning Resources

### In This Repository
- **QUICKSTART.md**: 5-minute hands-on tutorial
- **README.md**: Comprehensive documentation
- **examples/**: Sample bioink parameters

### External Resources
- **Original Paper**: Emmermacher et al. (2020), Biofabrication
- **Streamlit Docs**: https://docs.streamlit.io/
- **Python Tutorial**: https://docs.python.org/3/tutorial/

## 💡 Pro Tips

1. **Use Virtual Environment**: Keeps dependencies isolated
2. **Bookmark localhost:8501**: Easy access to app
3. **Try Example Parameters**: See `examples/bioink_parameters.txt`
4. **Export Your Results**: Use the download buttons in the app
5. **Experiment Safely**: All calculations are local, no data sent online

## 📞 Getting Help

### Within the App
- Hover over **ⓘ** icons for tooltips
- Expand **"Understanding the Physics"** section
- Check **"Cell Viability Assessment"** for recommendations

### Documentation
- Read **QUICKSTART.md** for immediate help
- Check **README.md** for detailed information
- Browse **examples/** for use cases

### Online Support
- **Issues**: Report bugs on GitHub Issues
- **Questions**: Ask on GitHub Discussions
- **Updates**: Check GitHub for latest version

## ✅ Success Checklist

Before you start, make sure:
- [ ] Python 3.8+ is installed
- [ ] You're in the repository directory
- [ ] You have internet connection (for first-time setup)
- [ ] Port 8501 is available

## 🎉 You're Ready!

Everything is set up and ready to use. Choose your platform above and start analyzing!

**Most Common Workflow:**
1. Run `setup.sh` or `setup.bat` (first time only)
2. Run `run.sh` or `run.bat` (every time)
3. Adjust parameters in sidebar
4. Analyze results
5. Export data

---

**Quick Commands:**

```bash
# Linux/macOS
./setup.sh && ./run.sh

# Windows
setup.bat && run.bat

# Manual (all platforms)
pip install -r requirements.txt
streamlit run app.py
```

**Need help?** Check QUICKSTART.md or README.md

**Happy bioprinting!** 🧬🖨️
