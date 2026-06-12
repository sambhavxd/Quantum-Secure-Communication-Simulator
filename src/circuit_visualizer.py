from qiskit import QuantumCircuit
import random

def generate_demo_circuit():

    bit = random.randint(0, 1)
    basis = random.randint(0, 1)

    qc = QuantumCircuit(1, 1)

    if bit == 1:
        qc.x(0)

    if basis == 1:
        qc.h(0)

    qc.measure(0, 0)

    return qc, bit, basis