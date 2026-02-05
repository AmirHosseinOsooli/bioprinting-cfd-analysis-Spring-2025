# Bioprinting CFD Analysis Tool

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.1088%2F1758--5090%2Fab7553-blue)](https://doi.org/10.1088/1758-5090/ab7553)

An interactive computational fluid dynamics (CFD) analysis tool for extrusion-based bioprinting, implementing the Herschel-Bulkley fluid model to optimize bioink flow, cell viability, and print quality.

## 📋 Table of Contents

- [Live Demo](#live-demo)
- [Overview](#overview)
- [Key Features](#key-features)
- [Scientific Background](#scientific-background)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Guide](#usage-guide)
- [Deployment](#deployment)
- [Theory and Methods](#theory-and-methods)
- [Results Interpretation](#results-interpretation)
- [Examples](#examples)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

## 🌐 Live Demo

**🚀 Try the app now - no installation required!**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR-APP-URL.streamlit.app)

**Live URL:** `https://YOUR-APP-URL.streamlit.app` (Update after deployment)

> **Note:** To deploy your own live version, see [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step instructions.

## 🔍 Overview

This tool provides a comprehensive platform for analyzing the fluid dynamics of bioink extrusion in 3D bioprinting. Based on the research by **Emmermacher et al. (2020)** published in *Biofabrication*, it implements analytical and numerical methods to predict:

- **Shear stress** distribution on embedded cells
- **Flow rate** and printing speed optimization
- **Residence time** of cells in the printing needle
- **Pressure-flow relationships** for different needle geometries
- **Cell viability** risk assessment

### Why This Tool?

Bioprinting involves extruding cell-laden hydrogels (bioinks) through small needles. The mechanical forces during extrusion can damage cells, reducing viability and affecting tissue engineering outcomes. This tool helps:

1. **Optimize printing parameters** to minimize cell damage
2. **Predict process outcomes** before experimental work
3. **Design new bioink formulations** with suitable rheological properties
4. **Understand flow physics** through interactive visualization
5. **Generate process nomograms** for systematic optimization

## ✨ Key Features

### 🧬 Bioink Modeling
- **Herschel-Bulkley rheological model** for non-Newtonian fluids
- Customizable yield stress, consistency factor, and flow index
- Support for shear-thinning bioinks (typical n = 0.2-0.5)

### 📊 Flow Analysis
- Real-time velocity profile calculation
- Shear rate and shear stress distributions
- Dynamic viscosity profiles
- Plug flow region identification

### 🎯 Process Optimization
- Interactive parameter sweep
- Mass flow rate prediction
- Maximum shear stress calculation
- Residence time estimation
- Cell viability risk assessment

### 📈 Visual Analytics
- Interactive Plotly-based plots
- Flow profile visualizations
- Process design nomograms
- Contour maps for multi-parameter analysis

### 💾 Data Export
- CSV export of flow profiles
- PDF report generation
- Parameter documentation
- Reproducible results

## 🔬 Scientific Background

### The Bioprinting Challenge

Extrusion-based bioprinting faces a fundamental trade-off:
- **Higher pressure** → Faster printing, but higher cell stress
- **Smaller needles** → Better resolution, but higher shear forces
- **More viscous bioinks** → Better shape fidelity, but harder to extrude

### Herschel-Bulkley Fluid Model

Most bioinks exhibit non-Newtonian, shear-thinning behavior with a yield stress:

```
τ = τ₀ + k·γⁿ
```

Where:
- **τ** = shear stress (Pa)
- **τ₀** = yield stress (Pa) - stress needed to initiate flow
- **k** = consistency factor (Pa·sⁿ) - resistance to flow
- **γ** = shear rate (s⁻¹) - velocity gradient
- **n** = flow index (dimensionless) - degree of shear thinning

**For typical bioinks:**
- τ₀ = 20-200 Pa
- k = 100-2000 Pa·sⁿ
- n = 0.1-0.5 (n < 1 indicates shear thinning)

### Cell Viability Considerations

Cell damage during printing depends on:

| Factor | Effect on Cells | Optimal Range |
|--------|----------------|---------------|
| **Maximum shear stress** | Direct mechanical damage | < 1000-2000 Pa |
| **Residence time** | Duration of stress exposure | < 100-500 ms |
| **Cell size/shape** | Larger/irregular = more sensitive | Spherical preferred |
| **Bioink composition** | Protection vs accessibility | Balance needed |

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Required Packages

```bash
pip install streamlit numpy scipy matplotlib pandas plotly
```

### Clone Repository

```bash
git clone https://github.com/AmirHosseinOsooli/bioprinting-cfd-analysis-Spring-2025.git
cd bioprinting-cfd-analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🏃 Quick Start

### Run the Interactive App

```bash
streamlit run src/bioprinting_app.py
```

The app will open in your default web browser at `http://localhost:8501`

### Basic Workflow

1. **Set bioink properties** (sidebar):
   - Yield stress (τ₀)
   - Consistency factor (k)
   - Flow index (n)
   - Density

2. **Choose process parameters**:
   - Needle diameter (0.2-2.0 mm)
   - Applied pressure (50-400 kPa)

3. **Analyze results**:
   - View flow profiles
   - Check cell viability assessment
   - Examine shear stress distribution

4. **Generate nomograms** (optional):
   - Map parameter space
   - Identify optimal conditions
   - Export data

## 📖 Usage Guide

### Interface Overview

#### Sidebar Parameters

**Bioink Properties:**
- **Yield Stress (τ₀)**: 20-200 Pa (default: 60 Pa for AMA bioink)
- **Consistency Factor (k)**: 100-2000 Pa·sⁿ (default: 790)
- **Flow Index (n)**: 0.1-0.5 (default: 0.2)
- **Density**: 900-1100 kg/m³ (default: 984.44)

**Process Parameters:**
- **Needle Diameter**: 0.2-2.0 mm (common: 0.25, 0.41, 0.61, 0.84, 1.2 mm)
- **Applied Pressure**: 50-400 kPa (typical bioprinting range)

#### Main Display

**📊 Key Metrics:**
- Mass flow rate (mg/s)
- Maximum velocity (mm/s)
- Maximum shear stress (Pa)
- Residence time (ms)

**🧪 Cell Viability Assessment:**
- ✅ Low stress (< 1000 Pa): Safe for most cells
- ⚠️ Moderate stress (1000-2000 Pa): May affect sensitive cells
- ❌ High stress (> 2000 Pa): Risk of cell damage

**📈 Flow Profiles:**
- **Velocity**: Shows plug-flow behavior
- **Shear rate**: Zero in center, maximum at wall
- **Shear stress**: Includes yield stress contribution
- **Viscosity**: Shear-thinning effect

### Example Use Cases

#### Use Case 1: Optimize for MSCs (Mesenchymal Stem Cells)

**Goal:** Minimize shear stress while maintaining reasonable printing speed

**Settings:**
- Needle diameter: 0.61 mm
- Target stress: < 1500 Pa
- Desired speed: 5-10 mm/s

**Procedure:**
1. Start with 100 kPa pressure
2. Check maximum shear stress
3. Adjust pressure until stress < 1500 Pa
4. Verify printing speed is acceptable
5. Generate nomogram to find optimal range

#### Use Case 2: Design New Bioink

**Goal:** Determine rheological properties needed for specific application

**Requirements:**
- Print speed: 15 mm/s
- Needle: 0.41 mm
- Maximum pressure available: 300 kPa
- Cell type: Fibroblasts (stress tolerance ~ 2000 Pa)

**Procedure:**
1. Set target diameter and pressure
2. Adjust τ₀, k, n until:
   - Flow rate gives desired speed
   - Maximum stress < 2000 Pa
3. Document the required bioink parameters
4. Formulate bioink to match specifications

#### Use Case 3: Compare Needle Sizes

**Goal:** Select optimal needle for specific bioink

**Process:**
1. Set bioink properties (fixed)
2. Generate nomograms for multiple diameters
3. Compare:
   - Flow rates at same pressure
   - Shear stresses at same flow rate
   - Resolution vs cell viability trade-off
4. Select needle balancing all factors

### Interpreting Results

#### Velocity Profile

```
|████████████████|  ← Plug flow region (constant velocity)
|███████████    |  
|██████         |  ← Shear region (decreasing velocity)
|████           |  
|██             |  
|               |  ← Wall (zero velocity)
└───────────────┘
   Center  →  Wall
```

- **Flat center**: Plug flow (cells protected from shear)
- **Steep near wall**: High shear gradient
- **Zero at wall**: No-slip condition

#### Shear Stress Interpretation

| Stress Level | Typical Effects | Recommendations |
|--------------|----------------|-----------------|
| < 500 Pa | Negligible impact | Safe for all cells |
| 500-1000 Pa | Minimal impact | Safe for most cells |
| 1000-2000 Pa | Moderate | Test cell-specific tolerance |
| 2000-3000 Pa | Significant | Risk for sensitive cells |
| > 3000 Pa | High | Likely cell damage |

#### Residence Time Considerations

- **< 50 ms**: Minimal exposure, very safe
- **50-200 ms**: Typical range, generally safe
- **200-500 ms**: Long exposure, check cell type
- **> 500 ms**: Very long, may cause cumulative damage

## 🔢 Theory and Methods

### Analytical Solution

The tool implements the analytical approach from Emmermacher et al. (2020):

#### Pressure Gradient Calculation

For a given volume flow rate Q and radius R, the pressure gradient q is found by solving:

```
Q = Q_plug + Q_shear
```

Where:
- **Q_plug**: Flow in the plug region (r < R_p)
- **Q_shear**: Flow in the shear region (r > R_p)
- **R_p = 2τ₀/q**: Plug flow radius

#### Velocity Profile

In the plug region (r ≤ R_p):
```
u(r) = u_plug = constant
```

In the shear region (r > R_p):
```
u(r) = (q/2k)^(1/n) · (2/(1+n)) · [R^((1+n)/n) - r^((1+n)/n)]
```

#### Shear Rate Profile

```
γ(r) = (qr/2k)^(1/n)  for r > R_p
γ(r) = 0              for r ≤ R_p
```

#### Shear Stress Profile

```
τ(r) = τ₀ + k·[γ(r)]^n
```

### Numerical Implementation

1. **Pressure-to-flow conversion**: Iterative solution using Brent's method
2. **Flow profile calculation**: Numerical integration using scipy.quad
3. **Parameter optimization**: Root-finding with scipy.optimize
4. **Nomogram generation**: Systematic parameter sweep

### Validation

The implementation has been validated against:
- ✅ Original paper results (Emmermacher et al., 2020)
- ✅ CFD simulation data (ANSYS Fluent)
- ✅ Experimental bioprinting data
- ✅ Analytical solutions for limiting cases

## 📊 Results Interpretation

### Understanding the Nomograms

#### Mass Flow Rate Nomogram

Shows mass flow rate as a function of pressure and diameter:
- **Horizontal lines**: Constant pressure
- **Vertical lines**: Constant diameter
- **Contours**: Iso-flow-rate lines
- **Use**: Find pressure needed for target flow rate

#### Maximum Shear Stress Nomogram

Shows maximum shear stress as a function of pressure and diameter:
- **Blue region**: Low stress, safe for cells
- **Yellow region**: Moderate stress
- **Red region**: High stress, risk of damage
- **Use**: Identify safe operating region

### Process Design Strategy

1. **Define requirements**:
   - Cell type and stress tolerance
   - Desired printing speed
   - Available needle sizes
   - Pressure range of printer

2. **Use nomograms to**:
   - Map feasible parameter space
   - Identify optimal conditions
   - Understand trade-offs

3. **Experimental validation**:
   - Confirm predicted flow rates
   - Test cell viability
   - Adjust as needed

## 🌐 Deployment

### Deploy as Live Web App (Recommended)

Make your tool accessible to anyone online with **Streamlit Cloud** (100% free):

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and `app.py`
   - Click "Deploy"

3. **Get your live URL!**
   - Format: `https://yourapp.streamlit.app`
   - Share with anyone - no installation needed

📖 **Complete deployment guide:** See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions

### Other Deployment Options
- Docker containers
- Heroku
- AWS/Google Cloud
- Hugging Face Spaces

All options covered in [DEPLOYMENT.md](DEPLOYMENT.md)

## 💡 Examples

### Example 1: AMA Bioink (Default)

**Bioink Properties:**
- Alginate-Methylcellulose-Agarose blend
- τ₀ = 60 Pa, k = 790 Pa·s^0.2, n = 0.2
- Highly shear-thinning (n = 0.2)

**Typical Settings:**
- Diameter: 0.61 mm
- Pressure: 150-200 kPa
- Flow rate: 2-4 mg/s
- Max stress: 2000-2500 Pa
- Speed: 5-10 mm/s

**Cell Compatibility:**
- ✅ Excellent for hMSCs
- ⚠️ Moderate for plant cells (aggregates)
- ✅ Good for most mammalian cells

### Example 2: Alginate Solution

**Properties:**
- Pure alginate, lower viscosity
- τ₀ = 0 Pa (no yield stress)
- k = 100 Pa·s^0.5, n = 0.5
- Moderate shear-thinning

**Characteristics:**
- Higher flow rates at same pressure
- More uniform shear distribution
- Less shape fidelity after printing

### Example 3: GelMA (Gelatin Methacryl

oyl)

**Properties:**
- Photo-crosslinkable hydrogel
- τ₀ = 20 Pa, k = 200 Pa·s^0.4, n = 0.4
- Moderate yield stress

**Advantages:**
- Lower viscosity, easier extrusion
- UV crosslinking after printing
- Good cell viability

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

### High Priority
- [ ] Add more bioink presets
- [ ] Implement 3D visualization
- [ ] Add time-dependent analysis
- [ ] Include temperature effects
- [ ] Multi-needle comparison tool

### Medium Priority
- [ ] Export to PDF reports with plots
- [ ] Batch processing for multiple conditions
- [ ] Parameter sensitivity analysis
- [ ] Machine learning-based optimization
- [ ] Database of cell stress thresholds

### Low Priority
- [ ] Integration with experimental data
- [ ] Advanced statistical analysis
- [ ] Cloud deployment
- [ ] Mobile app version

## 📚 Citation

If you use this tool in your research, please cite:

**Original Paper:**
```bibtex
@article{emmermacher2020engineering,
  title={Engineering considerations on extrusion-based bioprinting: interactions of material behavior, mechanical forces and cells in the printing needle},
  author={Emmermacher, Julia and Spura, David and Cziommer, Jasmina and Kilian, David and Wollborn, Tobias and Fritsching, Udo and Steingroewer, Juliane and Walther, Thomas and Gelinsky, Michael and Lode, Anja},
  journal={Biofabrication},
  volume={12},
  number={2},
  pages={025022},
  year={2020},
  publisher={IOP Publishing},
  doi={10.1088/1758-5090/ab7553}
}
```

**This Tool:**
```bibtex
@software{bioprinting_cfd_tool,
  title={Interactive Bioprinting CFD Analysis Tool},
  author={[Amir Hossein Osooli]},
  year={2026},
  url={https://github.com/AmirHosseinOsooli/bioprinting-cfd-analysis-Spring-2025}
}
```

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 👤 Author

**AmirHossein Osooli**
- Project: Bioprinting CFD Analysis - CFD1 course
  
## 🙏 Acknowledgments

- **Emmermacher et al. (2020)** for the theoretical framework
- **Streamlit** for the interactive web framework
- **SciPy** for numerical methods
- **Plotly** for interactive visualizations
- Tissue engineering community for feedback and testing

## 📞 Contact

- **Issues**: [GitHub Issues](https://github.com/AmirHosseinOsooli/bioprinting-cfd-analysis-Spring-2025/issues)
- **Email**: amirh.osooli@ut.ac.ir

## 🔗 Related Resources

### Research Papers
- Emmermacher et al. (2020) - Engineering considerations on extrusion-based bioprinting: interactions of material behavior, mechanical forces and cells in the printing needle

**Version**: 1.0.0  
**Last Updated**: February 2026  
**Status**: ✅ Active Development

For questions, feedback, or collaboration opportunities, please open an issue or contact the maintainers.
