from qiskit import QuantumCircuit

def encode_qubit(bit, basis):

    qc = QuantumCircuit(1, 1)

    if basis == 0:

        if bit == 1:
            qc.x(0)

    else:

        if bit == 0:
            qc.h(0)

        else:
            qc.x(0)
            qc.h(0)

    return qc