# 🧬 Bioprinting CFD Analysis Tool

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.1088%2F1758--5090%2Fab7553-blue)](https://doi.org/10.1088/1758-5090/ab7553)

> Interactive CFD analysis tool for extrusion-based bioprinting using the Herschel-Bulkley fluid model

## 🌐 Live Demo

**Try it now - No installation required!**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bioprinting-cfd.streamlit.app)

**Live URL:** https://bioprinting-cfd.streamlit.app

> Use the app directly in your browser - no Python, no installation needed!

---

## 📸 Screenshots

<div align="center">
  <img src="assets/nomogram_flow.png" alt="Mass Flow Rate Nomogram" width="45%">
  <img src="assets/nomogram_stress.png" alt="Shear Stress Nomogram" width="45%">
  <p><i>Example nomograms showing mass flow rate and maximum shear stress</i></p>
</div>

---

## 🎯 Quick Start

### Option 1: Use Live Web App (Recommended)
**Fastest - just click:**
1. Visit: https://bioprinting-cfd.streamlit.app
2. Adjust parameters in sidebar
3. Analyze results instantly

### Option 2: Run Locally
**For customization:**
```bash
# Clone repository
git clone https://github.com/AmirHosseinOsooli/bioprinting-cfd-analysis-Spring-2025.git
cd bioprinting-cfd-analysis-Spring-2025

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---

## 🔍 What Does This Tool Do?

Analyzes fluid flow of bioinks through printing needles to optimize:
- ✅ **Cell viability** - Minimize mechanical damage
- ✅ **Print quality** - Optimize flow parameters
- ✅ **Process efficiency** - Maximize printing speed
- ✅ **Parameter selection** - Visual nomograms for decision-making

### Key Features

- 🧬 **Herschel-Bulkley Model** - Non-Newtonian fluid behavior
- 📊 **Real-time Analysis** - Instant calculations
- 🎯 **Cell Viability Assessment** - Risk evaluation
- 📈 **Interactive Plots** - Velocity, shear stress, viscosity profiles
- 🗺️ **Process Nomograms** - Multi-parameter optimization maps
- 💾 **Data Export** - CSV and text reports

---

## 📚 Scientific Background

Based on: **Emmermacher et al. (2020)** - *Biofabrication* 12(2): 025022

### The Challenge

Bioprinting involves extruding cell-laden hydrogels through small needles. This creates a critical trade-off:
- **High pressure** → Faster printing BUT higher cell stress ❌
- **Small needles** → Better resolution BUT more shear forces ❌
- **This tool helps** → Find optimal balance ✅

### Herschel-Bulkley Model

```
τ = τ₀ + k·γⁿ
```

Where:
- **τ** = shear stress
- **τ₀** = yield stress (material starts to flow)
- **k** = consistency factor (resistance to flow)
- **γ** = shear rate
- **n** = flow index (shear thinning behavior)

### Analytical Solution

- ✅ Second-order accuracy (O(Δx²))
- ✅ Validated against CFD simulations
- ✅ Fast computation (< 1 second)
- ✅ No iterative solvers needed

---

## 🎮 How to Use

### 1. Set Bioink Properties (Sidebar)
- **Yield Stress (τ₀)**: 10-200 Pa
- **Consistency Factor (k)**: 100-2000 Pa·sⁿ
- **Flow Index (n)**: 0.1-1.0 (< 1 = shear thinning)
- **Density**: 800-1200 kg/m³

### 2. Choose Process Parameters
- **Needle Diameter**: 0.1-2.0 mm (common: 0.41, 0.61, 0.84 mm)
- **Applied Pressure**: 50-500 kPa

### 3. Analyze Results
- View key metrics (flow rate, max stress, residence time)
- Check cell viability assessment
- Examine flow profiles
- Generate optimization nomograms

### 4. Export Data
- Download flow profile data (CSV)
- Save analysis report (TXT)

---

## 📖 Example Use Cases

### Use Case 1: MSC Printing Optimization
**Goal:** Find safe parameters for mesenchymal stem cells

**Settings:**
- Bioink: AMA (τ₀=60, k=790, n=0.2)
- Target: τ_max < 1500 Pa
- Desired speed: > 5 mm/s

**Result:** Diameter = 0.61 mm, Pressure = 150 kPa ✅

### Use Case 2: New Bioink Design
**Goal:** Determine required rheological properties

**Requirements:**
- Print speed: 15 mm/s
- Needle: 0.41 mm
- Max pressure: 300 kPa
- Cell tolerance: 2000 Pa

**Result:** τ₀ ≤ 25 Pa, k ≤ 300 Pa·sⁿ, n ≈ 0.4 ✅

### Use Case 3: Multi-Parameter Comparison
**Goal:** Compare different needle sizes

**Method:**
1. Set bioink properties
2. Generate nomograms
3. Identify safe operating regions
4. Balance resolution vs viability

---

## 🔢 Default Parameters (AMA Bioink)

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| **τ₀** | 60 | Pa | Yield stress |
| **k** | 790 | Pa·sⁿ | Consistency factor |
| **n** | 0.2 | - | Flow index (shear thinning) |
| **ρ** | 984.4 | kg/m³ | Density |
| **D** | 0.61 | mm | Needle diameter |
| **Δp** | 200 | kPa | Applied pressure |

**Results:**
- Mass flow: ~3.5 mg/s
- Max velocity: ~12 mm/s
- Max shear stress: ~2800 Pa
- Residence time: ~90 ms

---

## 📊 Cell Viability Guidelines

| Shear Stress | Risk Level | Cell Types |
|--------------|------------|-----------|
| < 1000 Pa | ✅ Safe | All cell types |
| 1000-1500 Pa | ⚠️ Moderate | MSCs, fibroblasts OK |
| 1500-2000 Pa | ⚠️ Caution | Test specific cells |
| 2000-3000 Pa | ❌ High | Sensitive cells at risk |
| > 3000 Pa | ❌ Very High | Likely cell damage |

**Residence Time:**
- < 100 ms: ✅ Excellent
- 100-200 ms: ✅ Good
- 200-500 ms: ⚠️ Monitor
- > 500 ms: ❌ Reduce

---

## 🛠️ Technology Stack

- **Python 3.8+** - Core language
- **Streamlit** - Interactive web framework
- **NumPy** - Numerical computations
- **SciPy** - Optimization and integration
- **Plotly** - Interactive visualizations
- **Pandas** - Data manipulation

---

## 📦 Installation & Deployment

### Local Installation

```bash
# Clone repository
git clone https://github.com/AmirHosseinOsooli/bioprinting-cfd-analysis-Spring-2025.git
cd bioprinting-cfd-analysis-Spring-2025

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

### Deploy to Streamlit Cloud (Free)

1. Fork/clone this repository to your GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select repository and `app.py`
6. Deploy!

**See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions**

---

## 📁 Repository Structure

```
bioprinting-cfd-analysis/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── QUICKSTART.md              # 5-minute tutorial
├── DEPLOYMENT.md              # Deployment guide
├── LICENSE                     # MIT License
├── .streamlit/
│   └── config.toml            # Streamlit configuration
├── assets/
│   ├── nomogram_flow.png      # Example nomogram images
│   └── nomogram_stress.png
├── examples/
│   └── bioink_parameters.txt  # Sample bioink properties
└── docs/
    └── *.png                   # Additional documentation images
```

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Ideas for Contributions
- [ ] Add more bioink presets
- [ ] Implement 3D visualization
- [ ] Add temperature effects
- [ ] Include time-dependent analysis
- [ ] Multi-needle comparison
- [ ] ML-based optimization

---

## 📖 Citation

If you use this tool in your research, please cite:

**Original Paper:**
```bibtex
@article{emmermacher2020engineering,
  title={Engineering considerations on extrusion-based bioprinting},
  author={Emmermacher, Julia and Spura, David and others},
  journal={Biofabrication},
  volume={12},
  number={2},
  pages={025022},
  year={2020},
  doi={10.1088/1758-5090/ab7553}
}
```

**This Tool:**
```bibtex
@software{bioprinting_cfd_tool_2026,
  title={Interactive Bioprinting CFD Analysis Tool},
  author={Osooli, AmirHossein},
  year={2026},
  url={https://github.com/AmirHosseinOsooli/bioprinting-cfd-analysis-Spring-2025}
}
```

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Emmermacher et al. (2020)** for the theoretical framework
- **Streamlit** for the amazing web framework
- **SciPy** for numerical methods
- **Plotly** for interactive visualizations
- Tissue engineering community for feedback

---

## 📞 Support

- 📖 **Documentation**: See [README.md](README.md), [QUICKSTART.md](QUICKSTART.md)
- 🐛 **Issues**: [GitHub Issues](https://github.com/AmirHosseinOsooli/bioprinting-cfd-analysis-Spring-2025/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/AmirHosseinOsooli/bioprinting-cfd-analysis-Spring-2025/discussions)

---

## 🌟 Star History

If you find this tool useful, please ⭐ star the repository!

---

<div align="center">

**Made with ❤️ for the bioprinting community**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bioprinting-cfd.streamlit.app)

[Live Demo](https://bioprinting-cfd.streamlit.app) • [Documentation](README.md) • [Quick Start](QUICKSTART.md) • [Deploy](DEPLOYMENT.md)

</div>
