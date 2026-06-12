from qiskit_aer import AerSimulator

from .quantum_channel import encode_qubit
from .quantum_noise import create_noise_model

def measure_qubit_with_noise(
    bit,
    alice_basis,
    measurement_basis,
    noise_probability=0.05
):

    noise_model = create_noise_model(
        noise_probability
    )

    simulator = AerSimulator(
        noise_model=noise_model
    )

    qc = encode_qubit(
        bit,
        alice_basis
    )

    if measurement_basis == 1:
        qc.h(0)

    qc.measure(0, 0)

    result = simulator.run(
        qc,
        shots=1
    ).result()

    counts = result.get_counts()

    measured_bit = int(
        list(counts.keys())[0]
    )

    return measured_bit