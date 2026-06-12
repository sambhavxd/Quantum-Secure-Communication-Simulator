from qiskit_aer import AerSimulator
from .quantum_channel import encode_qubit

simulator = AerSimulator()

def measure_qubit(bit, alice_basis, measurement_basis):

    qc = encode_qubit(bit, alice_basis)

    if measurement_basis == 1:
        qc.h(0)

    qc.measure(0, 0)

    result = simulator.run(qc, shots=1).result()

    counts = result.get_counts()

    return int(list(counts.keys())[0])