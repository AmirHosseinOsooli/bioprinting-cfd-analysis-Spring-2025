import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, brentq
from scipy.integrate import quad
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings
import logging

# Suppress all warnings
warnings.filterwarnings('ignore')

# Suppress Streamlit warnings specifically
logging.getLogger('streamlit.runtime.scriptrunner_utils.script_run_context').setLevel(logging.ERROR)

import os
os.environ['PYTHONWARNINGS'] = 'ignore'

class BioPrintingCFD:
    """
    Interactive CFD Analysis for bioprinting based on Herschel-Bulkley fluid model
    Implementation based on Emmermacher et al. (2020) - Biofabrication
    """
    
    def __init__(self, tau_0=60, k=790, n=0.2, density=984.44):
        self.tau_0 = tau_0
        self.k = k
        self.n = n
        self.density = density
        
        # Needle geometry (conical needle from paper)
        self.inlet_radius = 5.0e-3  # 5 mm inlet radius
        self.cartridge_length = 15e-3  # 15 mm inlet section
        self.needle_length = 20e-3  # 20 mm needle length
    
    def herschel_bulkley_viscosity(self, shear_rate):
        """Calculate apparent viscosity using Herschel-Bulkley model"""
        if shear_rate <= 0:
            return 1e6  # Very high viscosity for zero shear rate
        return self.tau_0 / shear_rate + self.k * (shear_rate ** (self.n - 1))
    
    def herschel_bulkley_stress(self, shear_rate):
        """Calculate shear stress using Herschel-Bulkley model"""
        if shear_rate <= 0:
            return self.tau_0
        return self.tau_0 + self.k * (shear_rate ** self.n)
    
    def pressure_to_flow_rate(self, pressure_Pa, outlet_radius):
        """Convert pressure to volume flow rate using iterative solution"""
        def flow_rate_equation(Q):
            if Q <= 0:
                return pressure_Pa
            
            q = self.analytical_pressure_gradient(Q, outlet_radius)
            total_pressure = q * (self.cartridge_length + self.needle_length)
            return total_pressure - pressure_Pa
        
        try:
            Q_initial = 1e-9
            Q_max = 1e-6
            Q_solution = brentq(flow_rate_equation, 1e-12, Q_max, xtol=1e-12)
            return max(Q_solution, 0)
        except:
            return pressure_Pa * np.pi * outlet_radius**4 / (8 * self.k * self.needle_length)
    
    def analytical_pressure_gradient(self, volume_flow_rate, radius):
        """Calculate pressure gradient using analytical approach"""
        if volume_flow_rate <= 0:
            return 0
        
        def pressure_gradient_equation(q):
            if q <= 0:
                return volume_flow_rate
            
            R_p = 2 * self.tau_0 / q if q > 2 * self.tau_0 / radius else radius
            
            if R_p >= radius:
                u_plug = ((q * radius)**((1 + self.n)/self.n) / 
                         (2 * self.k)**(1/self.n)) * (2 / (1 + self.n))
                calculated_flow = np.pi * radius**2 * u_plug
                return calculated_flow - volume_flow_rate
            
            if R_p > 0:
                u_plug = ((q / (2 * self.k))**(1/self.n) * 
                         (2 / (1 + self.n)) * 
                         (radius**((1 + self.n)/self.n) - R_p**((1 + self.n)/self.n)))
                Q_plug = np.pi * R_p**2 * u_plug
            else:
                Q_plug = 0
            
            def integrand(r):
                if r <= R_p:
                    return 0
                u_local = ((q / (2 * self.k))**(1/self.n) * 
                          (2 / (1 + self.n)) * 
                          (radius**((1 + self.n)/self.n) - r**((1 + self.n)/self.n)))
                return 2 * np.pi * r * u_local
            
            if R_p < radius:
                Q_shear, _ = quad(integrand, R_p, radius, limit=50, epsabs=1e-12)
            else:
                Q_shear = 0
            
            total_flow = Q_plug + Q_shear
            return total_flow - volume_flow_rate
        
        try:
            q_char = self.tau_0 / radius
            q_initial = max(q_char, 1000)
            q_max = 1e8
            q_solution = brentq(pressure_gradient_equation, q_initial, q_max, xtol=1e-6)
            return q_solution
        except:
            return 8 * self.k * volume_flow_rate / (np.pi * radius**4)
    
    def calculate_velocity_profile(self, radius, pressure_gradient):
        """Calculate velocity profile at outlet"""
        if pressure_gradient <= 0:
            return np.zeros(50), np.zeros(50)
        
        r = np.linspace(0, radius, 50)
        u = np.zeros_like(r)
        
        R_p = 2 * self.tau_0 / pressure_gradient if pressure_gradient > 2 * self.tau_0 / radius else 0
        
        for i, r_pos in enumerate(r):
            if r_pos <= R_p:
                u_p = ((pressure_gradient / (2 * self.k))**(1/self.n) * 
                      (2 / (1 + self.n)) * 
                      (radius**((1 + self.n)/self.n) - R_p**((1 + self.n)/self.n)))
                u[i] = u_p
            else:
                u[i] = ((pressure_gradient / (2 * self.k))**(1/self.n) * 
                       (2 / (1 + self.n)) * 
                       (radius**((1 + self.n)/self.n) - r_pos**((1 + self.n)/self.n)))
        
        return r, u
    
    def calculate_shear_profile(self, radius, pressure_gradient):
        """Calculate shear rate and stress profiles"""
        r = np.linspace(0.001 * radius, radius, 50)
        shear_rate = np.zeros_like(r)
        shear_stress = np.zeros_like(r)
        
        R_p = 2 * self.tau_0 / pressure_gradient if pressure_gradient > 2 * self.tau_0 / radius else 0
        
        for i, r_pos in enumerate(r):
            if r_pos > R_p and pressure_gradient > 0:
                shear_rate[i] = (pressure_gradient * r_pos / (2 * self.k))**(1/self.n)
                shear_stress[i] = self.tau_0 + self.k * (shear_rate[i]**self.n)
            else:
                shear_rate[i] = 0
                shear_stress[i] = self.tau_0
        
        return r, shear_rate, shear_stress
    
    def create_nomogram_data(self, outlet_diameters, pressures):
        """Generate data for nomogram plots"""
        results = []
        
        for D in outlet_diameters:
            for p in pressures:
                outlet_radius = D / 2
                pressure_Pa = p * 1000
                
                volume_flow_rate = self.pressure_to_flow_rate(pressure_Pa, outlet_radius)
                q = self.analytical_pressure_gradient(volume_flow_rate, outlet_radius)
                
                r_vel, u_vel = self.calculate_velocity_profile(outlet_radius, q)
                r_shear, shear_rate, shear_stress = self.calculate_shear_profile(outlet_radius, q)
                
                u_max = np.max(u_vel) if len(u_vel) > 0 and np.max(u_vel) > 0 else 0
                gamma_max = np.max(shear_rate) if len(shear_rate) > 0 else 0
                tau_max = np.max(shear_stress) if len(shear_stress) > 0 else self.tau_0
                
                mass_flow_rate = self.density * volume_flow_rate * 1000000
                
                if u_max > 0:
                    avg_velocity = np.mean(u_vel[u_vel > 0]) if np.any(u_vel > 0) else u_max * 0.6
                    residence_time = (self.cartridge_length + self.needle_length) / avg_velocity
                else:
                    residence_time = 0
                
                results.append({
                    'diameter_mm': D * 1000,
                    'pressure_kPa': p,
                    'mass_flow_mg_s': mass_flow_rate,
                    'tau_max_Pa': tau_max,
                    'residence_time_s': residence_time * 1000
                })
        
        return pd.DataFrame(results)

# Streamlit App
def main():
    st.set_page_config(page_title="Bioprinting CFD Analysis Tool", 
                       page_icon="🧬", 
                       layout="wide")
    
    st.title("🧬 Interactive Bioprinting CFD Analysis Tool")
    st.markdown("""
    **Based on Emmermacher et al. (2020) - Herschel-Bulkley Fluid Model**
    
    This tool analyzes the fluid flow of bioinks through printing needles, helping optimize bioprinting processes for cell viability and print quality.
    """)
    
    # Sidebar for parameters
    st.sidebar.header("📊 Bioink Properties")
    
    # Bioink parameters
    tau_0 = st.sidebar.slider("Yield Stress τ₀ (Pa)", 
                             min_value=10.0, max_value=200.0, value=60.0, step=5.0,
                             help="Stress required to initiate flow")
    
    k = st.sidebar.slider("Consistency Factor k (Pa·sⁿ)", 
                         min_value=100.0, max_value=2000.0, value=790.0, step=50.0,
                         help="Material consistency parameter")
    
    n = st.sidebar.slider("Flow Index n (-)", 
                         min_value=0.1, max_value=1.0, value=0.2, step=0.05,
                         help="Shear thinning behavior (n<1)")
    
    density = st.sidebar.slider("Density (kg/m³)", 
                               min_value=800.0, max_value=1200.0, value=984.4, step=10.0)
    
    st.sidebar.header("⚙️ Process Parameters")
    
    # Process parameters
    diameter = st.sidebar.slider("Needle Diameter (mm)", 
                                min_value=0.1, max_value=2.0, value=0.61, step=0.05)
    
    pressure = st.sidebar.slider("Applied Pressure (kPa)", 
                                min_value=50.0, max_value=500.0, value=200.0, step=25.0)
    
    # Initialize CFD analysis
    cfd = BioPrintingCFD(tau_0=tau_0, k=k, n=n, density=density)
    
    # Main analysis
    outlet_radius = diameter / 2 * 1e-3  # Convert to meters
    pressure_Pa = pressure * 1000
    
    # Calculate flow parameters
    volume_flow_rate = cfd.pressure_to_flow_rate(pressure_Pa, outlet_radius)
    q = cfd.analytical_pressure_gradient(volume_flow_rate, outlet_radius)
    
    # Calculate profiles
    r_vel, u_vel = cfd.calculate_velocity_profile(outlet_radius, q)
    r_shear, shear_rate, shear_stress = cfd.calculate_shear_profile(outlet_radius, q)
    
    # Calculate key metrics
    u_max = np.max(u_vel) if len(u_vel) > 0 and np.max(u_vel) > 0 else 0
    gamma_max = np.max(shear_rate) if len(shear_rate) > 0 else 0
    tau_max = np.max(shear_stress) if len(shear_stress) > 0 else tau_0
    mass_flow_rate = density * volume_flow_rate * 1000000
    
    if u_max > 0:
        avg_velocity = np.mean(u_vel[u_vel > 0]) if np.any(u_vel > 0) else u_max * 0.6
        residence_time = (cfd.cartridge_length + cfd.needle_length) / avg_velocity
    else:
        residence_time = 0
    
    # Display key results
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Mass Flow Rate", f"{mass_flow_rate:.3f} mg/s")
    
    with col2:
        st.metric("Max Velocity", f"{u_max*1000:.2f} mm/s")
    
    with col3:
        st.metric("Max Shear Stress", f"{tau_max:.0f} Pa")
    
    with col4:
        st.metric("Residence Time", f"{residence_time*1000:.2f} ms")
    
    # Cell viability assessment
    st.subheader("🧪 Cell Viability Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if tau_max < 1000:
            st.success("✅ Low stress - Excellent for most cell types")
        elif tau_max < 2000:
            st.warning("⚠️ Moderate stress - May affect sensitive cells")
        else:
            st.error("❌ High stress - Risk of cell damage")
    
    with col2:
        if residence_time < 0.1:
            st.success("✅ Short exposure time")
        elif residence_time < 0.5:
            st.warning("⚠️ Moderate exposure time")
        else:
            st.error("❌ Long exposure time")
    
    # Flow profiles
    st.subheader("📈 Flow Profiles")
    
    # Create interactive plots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=['Velocity Profile', 'Shear Rate Profile', 
                       'Shear Stress Profile', 'Dynamic Viscosity Profile'],
        specs=[[{"secondary_y": False}, {"secondary_y": False}],
               [{"secondary_y": False}, {"secondary_y": True}]]
    )
    
    # Velocity profile
    fig.add_trace(
        go.Scatter(x=r_vel*1000, y=u_vel*1000, 
                  name='Velocity', line=dict(color='blue', width=3)),
        row=1, col=1
    )
    
    # Shear rate profile
    fig.add_trace(
        go.Scatter(x=r_shear*1000, y=shear_rate, 
                  name='Shear Rate', line=dict(color='green', width=3)),
        row=1, col=2
    )
    
    # Shear stress profile
    fig.add_trace(
        go.Scatter(x=r_shear*1000, y=shear_stress, 
                  name='Shear Stress', line=dict(color='red', width=3)),
        row=2, col=1
    )
    
    # Viscosity profile
    viscosity_profile = []
    for i, gamma in enumerate(shear_rate):
        if gamma > 0:
            visc = shear_stress[i] / gamma
        else:
            visc = 1e6
        viscosity_profile.append(min(visc, 1e6))
    
    fig.add_trace(
        go.Scatter(x=r_shear*1000, y=viscosity_profile, 
                  name='Viscosity', line=dict(color='purple', width=3)),
        row=2, col=2
    )
    
    # Update layout
    fig.update_xaxes(title_text="Radius (mm)", row=1, col=1)
    fig.update_xaxes(title_text="Radius (mm)", row=1, col=2)
    fig.update_xaxes(title_text="Radius (mm)", row=2, col=1)
    fig.update_xaxes(title_text="Radius (mm)", row=2, col=2)
    
    fig.update_yaxes(title_text="Velocity (mm/s)", row=1, col=1)
    fig.update_yaxes(title_text="Shear Rate (1/s)", row=1, col=2)
    fig.update_yaxes(title_text="Shear Stress (Pa)", row=2, col=1)
    fig.update_yaxes(title_text="Viscosity (Pa·s)", type="log", row=2, col=2)
    
    fig.update_layout(height=700, showlegend=False)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Nomogram section
    st.subheader("🎯 Process Design Nomograms")
    
    if st.button("Generate Nomograms"):
        with st.spinner("Generating nomograms..."):
            # Generate nomogram data
            diameters = np.linspace(0.2e-3, 1.5e-3, 8)
            pressures_range = np.linspace(50, 400, 10)
            
            nomogram_data = cfd.create_nomogram_data(diameters, pressures_range)
            
            # Create nomogram plots
            fig_nomogram = make_subplots(
                rows=1, cols=2,
                subplot_titles=['Mass Flow Rate (mg/s)', 'Maximum Shear Stress (Pa)']
            )
            
            # Prepare data for contour plots
            diameters_mm = diameters * 1000
            D_grid, P_grid = np.meshgrid(diameters_mm, pressures_range)
            
            # Mass flow rate contour
            flow_grid = np.zeros_like(D_grid)
            stress_grid = np.zeros_like(D_grid)
            
            for i, p in enumerate(pressures_range):
                for j, d_mm in enumerate(diameters_mm):
                    mask = (nomogram_data['diameter_mm'] == d_mm) & (nomogram_data['pressure_kPa'] == p)
                    if mask.any():
                        flow_grid[i,j] = nomogram_data[mask]['mass_flow_mg_s'].iloc[0]
                        stress_grid[i,j] = nomogram_data[mask]['tau_max_Pa'].iloc[0]
            
            # Add contour plots
            fig_nomogram.add_trace(
                go.Contour(x=diameters_mm, y=pressures_range, z=flow_grid.T,
                          colorscale='Blues', showscale=True),
                row=1, col=1
            )
            
            fig_nomogram.add_trace(
                go.Contour(x=diameters_mm, y=pressures_range, z=stress_grid.T,
                          colorscale='Reds', showscale=True),
                row=1, col=2
            )
            
            fig_nomogram.update_xaxes(title_text="Needle Diameter (mm)")
            fig_nomogram.update_yaxes(title_text="Applied Pressure (kPa)")
            fig_nomogram.update_layout(height=500)
            
            st.plotly_chart(fig_nomogram, use_container_width=True)
    
    # Educational content
    with st.expander("📚 Understanding the Physics"):
        st.markdown("""
        ### Herschel-Bulkley Model
        The bioink behavior is described by: **τ = τ₀ + k·γⁿ**
        
        - **τ₀ (Yield Stress)**: Minimum stress needed to start flow
        - **k (Consistency Factor)**: Controls flow resistance
        - **n (Flow Index)**: Determines shear thinning behavior (n < 1)
        
        ### Plug Flow Behavior
        - **Central Region**: Material moves as rigid plug (low shear)
        - **Wall Region**: High shear gradients for flow
        - **Cell Protection**: Most cells experience gentle conditions
        
        ### Process Optimization
        - **Lower pressures**: Reduce cell damage but slower printing
        - **Larger diameters**: Higher flow rates but lower resolution
        - **Bioink properties**: Balance printability and biocompatibility
        """)
    
    # Data export
    st.subheader("💾 Export Results")
    
    # Prepare export data
    export_data = {
        'radius_mm': r_vel * 1000,
        'velocity_mm_s': u_vel * 1000,
        'shear_rate_1_s': np.interp(r_vel, r_shear, shear_rate),
        'shear_stress_Pa': np.interp(r_vel, r_shear, shear_stress)
    }
    export_df = pd.DataFrame(export_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Download Profile Data"):
            csv = export_df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"bioprinting_profiles_D{diameter}mm_P{pressure}kPa.csv",
                mime="text/csv"
            )
    
    with col2:
        # Summary report
        summary_text = f"""
        Bioprinting Analysis Report
        ==========================
        
        Bioink Properties:
        - Yield Stress: {tau_0} Pa
        - Consistency Factor: {k} Pa·s^{n}
        - Flow Index: {n}
        - Density: {density} kg/m³
        
        Process Parameters:
        - Needle Diameter: {diameter} mm
        - Applied Pressure: {pressure} kPa
        
        Results:
        - Mass Flow Rate: {mass_flow_rate:.3f} mg/s
        - Maximum Velocity: {u_max*1000:.2f} mm/s
        - Maximum Shear Stress: {tau_max:.0f} Pa
        - Residence Time: {residence_time*1000:.2f} ms
        """
        
        st.download_button(
            label="Download Report",
            data=summary_text,
            file_name=f"bioprinting_report_D{diameter}mm_P{pressure}kPa.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()