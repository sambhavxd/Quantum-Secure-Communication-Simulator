# Quantum Secure Communication Simulator

## Overview

A Quantum Key Distribution (QKD) simulator implementing the BB84 protocol using Qiskit.

Features:

- BB84 Quantum Key Distribution
- Intercept-Resend (Eve) Attack Simulation
- Quantum Bit Error Rate (QBER) Analysis
- Quantum Noise Modeling
- Security Operations Center Dashboard
- Statistical Security Validation

## Technologies

- Python
- Qiskit
- Streamlit
- Plotly
- NumPy

## Results

- No Eve: ~0% QBER
- Noise Only: ~5% QBER
- Eve Attack: ~25% QBER
- Eve + Noise: ~28% QBER

Consistent with theoretical BB84 predictions.

## Run Dashboard

```bash
streamlit run dashboard_soc_v4.py
```