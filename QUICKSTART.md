# Quick Start Guide

Get the Bioprinting CFD Analysis Tool running in **5 minutes**!

## 🚀 Installation (2 minutes)

### Step 1: Prerequisites

Make sure you have Python 3.8+ installed:
```bash
python --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)

### Step 2: Clone or Download

**Option A - Git:**
```bash
git clone https://github.com/yourusername/bioprinting-cfd-analysis.git
cd bioprinting-cfd-analysis
```

**Option B - Download ZIP:**
1. Download ZIP from GitHub
2. Extract to your desired location
3. Open terminal/command prompt in that folder

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🎯 First Analysis (3 minutes)

### Launch the App

```bash
streamlit run src/bioprinting_app.py
```

Your browser will automatically open to `http://localhost:8501`

### Default Example: AMA Bioink

The app loads with default settings for AMA bioink (Alginate-Methylcellulose-Agarose):

**Bioink Properties:**
- Yield Stress (τ₀): 60 Pa
- Consistency Factor (k): 790 Pa·s^0.2
- Flow Index (n): 0.2
- Density: 984.44 kg/m³

**Process Parameters:**
- Needle Diameter: 0.61 mm
- Applied Pressure: 150 kPa

### What You'll See

**📊 Key Metrics** (top of page):
```
Mass Flow Rate: ~2.5 mg/s
Maximum Velocity: ~8.5 mm/s
Maximum Shear Stress: ~2300 Pa
Residence Time: ~100 ms
```

**🧪 Cell Viability**:
- ⚠️ Moderate stress - May affect sensitive cells

**📈 Flow Profiles**:
- 4 interactive plots showing velocity, shear rate, shear stress, and viscosity

## 🎮 Try These Quick Experiments

### Experiment 1: Change Needle Size

1. **Sidebar** → Needle Diameter
2. Change from 0.61 mm to **0.25 mm** (smaller)
3. Click anywhere to update

**Observe:**
- ✅ Flow rate decreases dramatically
- ❌ Shear stress increases
- ⚠️ Cell viability risk increases

### Experiment 2: Adjust Pressure

1. Keep diameter at 0.25 mm
2. **Sidebar** → Applied Pressure
3. Reduce from 150 kPa to **100 kPa**

**Observe:**
- ✅ Shear stress decreases
- ✅ Cell viability improves
- ❌ Printing speed reduces

### Experiment 3: Generate Nomograms

1. Scroll to **"Process Design Nomograms"** section
2. Click **"Generate Nomograms"** button
3. Wait 10-20 seconds

**Result:**
- Two contour plots showing how flow rate and shear stress vary with diameter and pressure
- Use these to find optimal parameters!

## 📖 Understanding Your Results

### Key Metrics Explained

| Metric | What It Means | Typical Range |
|--------|---------------|---------------|
| **Mass Flow Rate** | How fast bioink is extruded | 1-10 mg/s |
| **Maximum Velocity** | Fastest speed in needle center | 5-20 mm/s |
| **Maximum Shear Stress** | Highest force on cells at wall | < 2000 Pa ideal |
| **Residence Time** | How long cells are stressed | < 200 ms ideal |

### Flow Profile Interpretation

```
Velocity Profile:
|████████████|  ← Flat region = plug flow (cells safe!)
|██████      |  ← Curved region = shear zone
|████        |  
|██          |  
|            |  ← Wall (zero velocity)
└────────────┘
  Center → Wall
```

**Plug Flow Region**: Most cells travel here with minimal shear stress!

### Cell Viability Zones

🟢 **Green Zone** (τ < 1000 Pa):
- Safe for ALL cell types
- MSCs, fibroblasts, chondrocytes

🟡 **Yellow Zone** (1000-2000 Pa):
- Safe for MOST cell types
- Test your specific cells
- May affect plant cell aggregates

🔴 **Red Zone** (> 2000 Pa):
- Risk of cell damage
- Reduce pressure or increase diameter
- Consider different bioink

## 🔧 Quick Parameter Guide

### For Different Cell Types

**Mammalian Stem Cells (MSCs):**
- Target stress: < 1500 Pa
- Typical diameter: 0.41-0.61 mm
- Pressure range: 100-200 kPa

**Fibroblasts:**
- Target stress: < 2000 Pa
- Typical diameter: 0.41-0.84 mm
- Pressure range: 100-250 kPa

**Plant Cells (aggregated):**
- Target stress: < 1300 Pa (more sensitive!)
- Typical diameter: 0.61-0.84 mm
- Pressure range: 50-150 kPa

### Troubleshooting

#### Problem: App won't start
```bash
# Check Streamlit is installed
pip show streamlit

# Reinstall if needed
pip install streamlit --upgrade
```

#### Problem: "Module not found" error
```bash
# Install all dependencies
pip install -r requirements.txt
```

#### Problem: Plots not showing
- Refresh browser (F5)
- Clear browser cache
- Try different browser (Chrome recommended)

#### Problem: App is slow
- Reduce number of nomogram points
- Close other applications
- Use faster computer if available

## 💡 Next Steps

### Learn More
1. Read the full [README.md](README.md) for detailed documentation
2. Check [docs/THEORY.md](docs/THEORY.md) for mathematical background
3. Explore [examples/](examples/) for use cases

### Customize for Your Bioink
1. Measure rheological properties of your bioink
2. Input τ₀, k, n into the sidebar
3. Generate nomograms for your specific case
4. Validate with experimental printing tests

### Export Your Data
1. Scroll to **"Export Results"** section
2. Click **"Download Profile Data"** for CSV
3. Click **"Download Report"** for text summary

## 📞 Get Help

- **Documentation**: [README.md](README.md)
- **Issues**: [GitHub Issues](https://github.com/yourusername/bioprinting-cfd-analysis/issues)
- **Questions**: [GitHub Discussions](https://github.com/yourusername/bioprinting-cfd-analysis/discussions)

## 🎉 Success!

You're now analyzing bioprinting processes like a pro!

**Quick Reference Commands:**
```bash
# Start the app
streamlit run src/bioprinting_app.py

# Update dependencies
pip install -r requirements.txt --upgrade

# Check Python version
python --version
```

---

**Estimated Time**: 5 minutes total
- Installation: 2 minutes
- First analysis: 3 minutes

**Difficulty**: 🟢 Beginner-Friendly

Happy bioprinting! 🧬🖨️
