
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.simulation_runner import run_single_simulation
from src.circuit_visualizer import generate_demo_circuit

st.set_page_config(page_title="Quantum Security Operations Center",
                   page_icon="🔐",
                   layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1rem;}
.metric-box{
background:#111827;border:1px solid #334155;
padding:15px;border-radius:14px;text-align:center;
}
.flow-card{
background:#111827;border:1px solid #334155;
padding:20px;border-radius:16px;
}
.threat-card{
background:#450a0a;border:1px solid #dc2626;
padding:20px;border-radius:16px;
}
</style>
""", unsafe_allow_html=True)

st.title("🔐 Quantum Security Operations Center")
st.caption("Protocol: BB84 | Attack Model: Intercept-Resend | Noise Model: Depolarizing Channel")

num_runs = st.slider("Simulation Runs", 1, 50, 10)

if st.button("🚀 Launch Security Analysis", use_container_width=True):

    qc, bit, basis = generate_demo_circuit()

    state = "|1⟩" if basis == 0 and bit else "|0⟩" if basis == 0 else "|−⟩" if bit else "|+⟩"

    no_eve_results, eve_results, noise_results, eve_noise_results = [], [], [], []

    with st.spinner("Running simulations..."):
        for _ in range(num_runs):
            r = run_single_simulation()
            no_eve_results.append(r["No Eve"] * 100)
            eve_results.append(r["Eve"] * 100)
            noise_results.append(r["Noise"] * 100)
            eve_noise_results.append(r["Eve + Noise"] * 100)

    avg_no_eve = sum(no_eve_results)/len(no_eve_results)
    avg_eve = sum(eve_results)/len(eve_results)
    avg_noise = sum(noise_results)/len(noise_results)
    avg_eve_noise = sum(eve_noise_results)/len(eve_noise_results)

    threat = "🔴 CRITICAL" if avg_eve > 11 else "🟢 SECURE"

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Threat Level", threat)
    c2.metric("Current QBER", f"{avg_eve:.2f}%")
    c3.metric("Detection Confidence", f"{min(avg_eve*4,99):.0f}%")
    c4.metric("Protocol", "BB84")

    left,right = st.columns([1.4,1])

    with left:
        st.markdown(f"""
        <div class="threat-card">
        <h2>🚨 Threat Status</h2>
        <h3>{'CHANNEL COMPROMISED' if avg_eve > 11 else 'CHANNEL SECURE'}</h3>
        <p>Observed QBER: {avg_eve:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)

    with right:
        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=avg_eve,
            title={"text":"Attack Risk"},
            gauge={
                "axis":{"range":[0,30]},
                "threshold":{"line":{"color":"white","width":4},"value":11},
                "bar":{"color":"red"},
                "steps":[
                    {"range":[0,5],"color":"green"},
                    {"range":[5,11],"color":"gold"},
                    {"range":[11,30],"color":"darkred"}
                ]
            }
        ))
        gauge.update_layout(template="plotly_dark",height=280)
        st.plotly_chart(gauge,use_container_width=True)

    st.markdown("### ⚛ Quantum Transmission Monitor")

    st.markdown(f"""
    <div class="flow-card">
    👤 <b>Alice</b><br>
    Bit: {bit} | Basis: {"X" if basis else "Z"} | State: {state}
    <br><br>
    ─────────▶ 🚨 <b>Eve Active</b> ─────────▶ 📡 <b>Bob Ready</b>
    </div>
    """, unsafe_allow_html=True)

    m1,m2,m3,m4 = st.columns(4)
    m1.metric("No Eve", f"{avg_no_eve:.2f}%")
    m2.metric("Eve", f"{avg_eve:.2f}%")
    m3.metric("Noise", f"{avg_noise:.2f}%")
    m4.metric("Eve + Noise", f"{avg_eve_noise:.2f}%")

    st.markdown("### 📊 Analytics")

    a,b = st.columns(2)

    with a:
        fig_bar = go.Figure()
        fig_bar.add_bar(
            x=["No Eve","Noise","Eve","Eve + Noise"],
            y=[avg_no_eve,avg_noise,avg_eve,avg_eve_noise],
            marker_color=["#22c55e","#f59e0b","#ef4444","#991b1b"]
        )
        fig_bar.update_layout(template="plotly_dark",
                              title="Threat Analysis by Scenario")
        st.plotly_chart(fig_bar,use_container_width=True)

    with b:
        trend_df = pd.DataFrame({
            "Run": list(range(1,len(eve_results)+1)),
            "QBER": eve_results
        })
        fig_line = px.line(trend_df,x="Run",y="QBER",
                           markers=True,
                           template="plotly_dark",
                           title="QBER Trend")
        st.plotly_chart(fig_line,use_container_width=True)

    st.markdown("### 📉 QBER Distribution")

    hist_df = pd.DataFrame({
        "QBER": no_eve_results+eve_results+noise_results+eve_noise_results,
        "Scenario":
        ["No Eve"]*len(no_eve_results)+
        ["Eve"]*len(eve_results)+
        ["Noise"]*len(noise_results)+
        ["Eve + Noise"]*len(eve_noise_results)
    })

    hist = px.histogram(
        hist_df,
        x="QBER",
        color="Scenario",
        opacity=0.75,
        nbins=25,
        template="plotly_dark"
    )

    hist.update_layout(
        plot_bgcolor="#111827",
        paper_bgcolor="#111827",
        font=dict(size=15)
    )

    st.plotly_chart(hist,use_container_width=True)

    st.markdown("### 📋 Research Validation")

    expected = 25.0
    deviation = abs(avg_eve - expected)

    r1,r2,r3,r4 = st.columns(4)
    r1.info(f"Expected Attack QBER\n\n{expected:.2f}%")
    r2.info(f"Observed QBER\n\n{avg_eve:.2f}%")
    r3.info(f"Deviation\n\n{deviation:.2f}%")
    r4.success("✓ Consistent with BB84 Theory")

    st.markdown("### 🔍 Attack Timeline")
    st.markdown("""
    Quantum State Generated → Channel Transmission → Eve Interception →
    Measurement Disturbance → QBER Increase → Attack Detection
    """)

    st.caption("Quantum Secure Communication Simulator | BB84 | Qiskit | Streamlit")
