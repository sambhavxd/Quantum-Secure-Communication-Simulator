from qiskit_aer.noise import NoiseModel
from qiskit_aer.noise import depolarizing_error

def create_noise_model(probability=0.05):

    noise_model = NoiseModel()

    error = depolarizing_error(
        probability,
        1
    )

    noise_model.add_all_qubit_quantum_error(
        error,
        ['x', 'h']
    )

    return noise_model