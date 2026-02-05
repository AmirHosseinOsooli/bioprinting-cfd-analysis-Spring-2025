# Theoretical Background and Mathematical Methods

## Table of Contents
- [Introduction](#introduction)
- [Rheological Models](#rheological-models)
- [Fluid Dynamics in Needles](#fluid-dynamics-in-needles)
- [Analytical Solution](#analytical-solution)
- [Cell Mechanics](#cell-mechanics)
- [Process Optimization](#process-optimization)
- [References](#references)

## Introduction

This document provides the mathematical and physical foundations for the bioprinting CFD analysis tool, based on the research by Emmermacher et al. (2020).

### Bioprinting Context

Extrusion-based bioprinting involves:
1. Loading cell-laden hydrogel (bioink) into a cartridge
2. Applying pneumatic pressure to the cartridge
3. Forcing bioink through a conical printing needle
4. Depositing continuous strands layer-by-layer

**Key Challenge**: Balance between:
- High printing speed (process efficiency)
- Low mechanical stress (cell viability)
- Good shape fidelity (print quality)

## Rheological Models

### Newton's Law (Not Applicable for Bioinks)

For Newtonian fluids (water, oils):
```
τ = μ·γ̇
```
- τ = shear stress (Pa)
- μ = dynamic viscosity (Pa·s)
- γ̇ = shear rate (s⁻¹)

**Problem**: Bioinks are NOT Newtonian!
- Viscosity changes with shear rate
- Exhibit yield stress (must overcome to flow)
- Show viscoelastic behavior

### Power Law Model (Too Simple)

For shear-thinning fluids:
```
τ = k·γ̇ⁿ
```
- k = consistency factor (Pa·sⁿ)
- n = flow index (dimensionless)
- n < 1: shear thinning
- n = 1: Newtonian
- n > 1: shear thickening

**Limitation**: No yield stress term!

### Herschel-Bulkley Model (Best for Bioinks)

Combines yield stress and power law:
```
τ = τ₀ + k·γ̇ⁿ
```

**Physical Meaning**:
- **τ₀** (yield stress): Minimum stress to initiate flow
  - Caused by network structure (polymers, cells)
  - Must be overcome to break gel structure
  
- **k** (consistency factor): Resistance to flow
  - Similar to viscosity but shear-dependent
  - Higher k = more viscous bioink
  
- **n** (flow index): Degree of shear thinning
  - n < 1: Shear thinning (typical for bioinks)
  - Lower n = stronger shear thinning
  - n = 0.2-0.5 for most bioinks

### Typical Parameter Ranges

| Bioink Type | τ₀ (Pa) | k (Pa·sⁿ) | n | Reference |
|-------------|---------|-----------|---|-----------|
| AMA | 60 | 790 | 0.2 | Emmermacher 2020 |
| Alginate (3%) | 0-20 | 50-200 | 0.4-0.6 | Various |
| GelMA (5%) | 10-30 | 100-500 | 0.3-0.5 | Various |
| Collagen | 5-15 | 20-100 | 0.5-0.7 | Various |
| Methylcellulose | 0-10 | 50-150 | 0.4-0.6 | Emmermacher 2020 |

## Fluid Dynamics in Needles

### Governing Equations

**Continuity Equation** (Conservation of Mass):
```
∇·u = 0  (incompressible flow)
```

**Momentum Equation** (Conservation of Momentum):
```
ρ(∂u/∂t + u·∇u) = -∇p + ∇·τ + ρg
```

**Assumptions for Bioprinting**:
1. Steady-state flow (∂u/∂t = 0)
2. Laminar flow (Re < 2300)
3. Axisymmetric geometry
4. No gravity effects in needle
5. Isothermal (constant temperature)
6. Incompressible fluid

### Reynolds Number

```
Re = ρ·u·D/μ
```

For typical bioprinting:
- ρ ≈ 1000 kg/m³
- u ≈ 0.01 m/s
- D ≈ 0.5 mm
- μ ≈ 1-100 Pa·s (apparent)

→ Re ≈ 0.05-5 << 2300 (laminar flow confirmed!)

### Plug Flow Phenomenon

Unlike Newtonian fluids (parabolic profile), Herschel-Bulkley fluids exhibit **plug flow**:

```
        Newtonian          Herschel-Bulkley
         Profile             Profile
            
       ___    ___         _______
      /   \  /   \       |       |
     /     \/     \      |  Plug | 
    /             \     |    Flow |
   /               \    |  Region |
  /                 \  |          |
 /___________________\|____________|
  Parabolic shape      Flat center

   Maximum at center    Constant in center
   Zero at wall         Steep gradient at wall
```

**Plug Flow Region**:
- Radius: R_p = 2τ₀/q
- Velocity: constant (u_plug)
- Shear stress: τ = τ₀ (at yield point)
- Shear rate: γ̇ = 0

**Shear Region** (R_p < r < R):
- Velocity: decreases to zero at wall
- Shear stress: τ > τ₀
- Shear rate: γ̇ > 0

**Cell Protection**: Most cells travel in plug region with minimal shear!

## Analytical Solution

### Problem Statement

Given:
- Bioink properties: τ₀, k, n, ρ
- Needle geometry: D_out, L
- Applied pressure: Δp

Find:
- Volume flow rate: Q
- Velocity profile: u(r)
- Shear stress profile: τ(r)
- Maximum shear stress: τ_max

### Solution Method

The analytical approach follows these steps:

#### Step 1: Pressure Gradient

For a given volume flow rate Q and radius R, find pressure gradient q:

```
Q = ∫₀^R 2πr·u(r) dr
```

Split into plug and shear regions:

```
Q = Q_plug + Q_shear
```

**Plug region contribution** (0 ≤ r ≤ R_p):
```
Q_plug = πR_p²·u_plug
```

where plug radius:
```
R_p = 2τ₀/q
```

and plug velocity:
```
u_plug = (q/2k)^(1/n) · (2/(1+n)) · [R^((1+n)/n) - R_p^((1+n)/n)]
```

**Shear region contribution** (R_p < r ≤ R):
```
Q_shear = ∫_{R_p}^R 2πr·u(r) dr
```

where velocity in shear region:
```
u(r) = (q/2k)^(1/n) · (2/(1+n)) · [R^((1+n)/n) - r^((1+n)/n)]
```

#### Step 2: Iterative Solution

For given Δp, find Q such that:
```
Δp = q·L
```

Use numerical root-finding (Brent's method) to solve.

#### Step 3: Velocity Profile

Once q is known, calculate u(r):

```python
def velocity_profile(r, q, R):
    R_p = 2 * tau_0 / q
    
    if r <= R_p:
        # Plug region
        u = u_plug
    else:
        # Shear region
        u = (q/(2*k))**(1/n) * (2/(1+n)) * (R**((1+n)/n) - r**((1+n)/n))
    
    return u
```

#### Step 4: Shear Rate Profile

```python
def shear_rate(r, q):
    R_p = 2 * tau_0 / q
    
    if r <= R_p:
        gamma = 0  # No shear in plug
    else:
        gamma = (q*r/(2*k))**(1/n)
    
    return gamma
```

#### Step 5: Shear Stress Profile

```python
def shear_stress(r, q):
    gamma = shear_rate(r, q)
    
    if gamma == 0:
        tau = tau_0  # Yield stress
    else:
        tau = tau_0 + k * gamma**n  # Herschel-Bulkley
    
    return tau
```

### Maximum Values

**Maximum velocity** (at centerline):
```
u_max = u(r=0) = u_plug
```

**Maximum shear rate** (at wall):
```
γ_max = (q·R/(2k))^(1/n)
```

**Maximum shear stress** (at wall):
```
τ_max = τ₀ + k·γ_max^n = q·R/2
```

### Residence Time

Average time cells spend in needle:
```
t_res = L/u_avg
```

where average velocity:
```
u_avg = Q/(π·R²)
```

## Cell Mechanics

### Cell as Viscoelastic Material

Cells are not solid or liquid, but **viscoelastic**:
- Elastic response to fast deformation
- Viscous response to slow deformation
- Time-dependent behavior

### Mechanical Cell Damage Mechanisms

1. **Membrane rupture**:
   - High shear stress tears cell membrane
   - Critical stress: 1000-3000 Pa (cell-dependent)
   
2. **Cytoskeleton disruption**:
   - Shear forces disrupt internal structure
   - Can lead to apoptosis

3. **Osmotic stress**:
   - Pressure gradients affect cell volume
   - Secondary effect in bioprinting

### Cell Size and Shape Effects

**Size**:
- Larger cells experience more force
- Effective stress ∝ cell diameter
- Plant cells (10-100 μm) > mammalian cells (10-20 μm)

**Shape**:
- Spherical cells (low stress)
- Elongated cells (high stress)
- Irregular shapes (intermediate)

### Critical Parameters

| Parameter | Effect | Threshold |
|-----------|--------|-----------|
| τ_max | Direct damage | < 1000-2000 Pa |
| t_res | Exposure time | < 100-500 ms |
| γ_max | Rate of deformation | < 1000-5000 s⁻¹ |
| Cell size | Stress amplification | Smaller is better |

### Viability Prediction

Simple model:
```
V = V₀ · exp(-k_damage · τ_max · t_res)
```

where:
- V = final viability (%)
- V₀ = initial viability (%)
- k_damage = damage rate constant (cell-specific)
- τ_max = maximum shear stress (Pa)
- t_res = residence time (s)

## Process Optimization

### Multi-Objective Optimization

**Objectives** (often conflicting):
1. Maximize printing speed
2. Minimize cell damage
3. Maximize shape fidelity
4. Minimize bioink consumption

**Constraints**:
- Maximum available pressure
- Minimum/maximum needle sizes
- Cell viability threshold
- Bioink rheological properties

### Nomogram Approach

Generate 2D maps of:
- Mass flow rate vs (D, Δp)
- Maximum stress vs (D, Δp)
- Residence time vs (D, Δp)

**Advantages**:
- Visual parameter selection
- Quick identification of feasible region
- Understanding trade-offs

### Optimization Strategy

1. **Define requirements**:
   - Cell type and tolerance
   - Desired print speed
   - Available equipment

2. **Measure bioink properties**:
   - Rheometry to get τ₀, k, n
   - Density measurement

3. **Generate nomograms**:
   - Use this tool
   - Map parameter space

4. **Select optimal point**:
   - Balance objectives
   - Consider constraints

5. **Validate experimentally**:
   - Test selected parameters
   - Measure actual viability
   - Adjust if needed

### Example: MSC Printing

**Requirements**:
- Cell: Human MSCs
- Tolerance: τ < 1500 Pa
- Speed: > 5 mm/s
- Pressure: < 300 kPa

**Solution**:
1. Measure AMA properties (τ₀=60, k=790, n=0.2)
2. Generate nomogram
3. Find region where:
   - τ_max < 1500 Pa
   - u_avg > 5 mm/s
   - Δp < 300 kPa
4. Select: D = 0.61 mm, Δp = 150 kPa
5. Predicted: τ_max ≈ 1400 Pa, u_avg ≈ 8 mm/s ✓

## References

### Primary References

1. **Emmermacher, J., et al. (2020)**. Engineering considerations on extrusion-based bioprinting: interactions of material behavior, mechanical forces and cells in the printing needle. *Biofabrication*, 12(2), 025022.

2. **Herschel, W. H., & Bulkley, R. (1926)**. Konsistenzmessungen von Gummi-Benzollösungen. *Kolloid-Zeitschrift*, 39(4), 291-300.

3. **Bird, R. B., Armstrong, R. C., & Hassager, O. (1987)**. *Dynamics of Polymeric Liquids*. Volume 1: Fluid Mechanics. Wiley.

### Bioprinting Mechanics

4. **Paxton, N., et al. (2017)**. Proposal to assess printability of bioinks for extrusion-based bioprinting and evaluation of rheological properties governing bioprintability. *Biofabrication*, 9(4), 044107.

5. **Blaeser, A., et al. (2016)**. Controlling shear stress in 3D bioprinting is a key factor to balance printing resolution and stem cell integrity. *Advanced Healthcare Materials*, 5(3), 326-333.

6. **Li, M., et al. (2011)**. Effect of needle geometry on flow rate and cell damage in the dispensing-based biofabrication process. *Biotechnology Progress*, 27(6), 1777-1784.

### Cell Mechanics

7. **Barbee, K. A. (2006)**. Mechanical cell injury. *Annals of the New York Academy of Sciences*, 1066(1), 67-84.

8. **Mao, S., et al. (2015)**. The influence of printing parameters on cell survival rate and printability in microextrusion-based 3D cell printing technology. *Biofabrication*, 7(4), 045002.

### Rheology

9. **Chhabra, R. P., & Richardson, J. F. (2011)**. *Non-Newtonian Flow and Applied Rheology: Engineering Applications*. Butterworth-Heinemann.

10. **Malkin, A. Y., & Isayev, A. I. (2017)**. *Rheology: Concepts, Methods, and Applications*. ChemTec Publishing.

---

**Document Version**: 1.0  
**Last Updated**: February 2026  
**Based on**: Emmermacher et al. (2020) and cited references
