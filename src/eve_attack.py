from .measure import measure_qubit

def eve_intercept(bit, alice_basis, eve_basis):

    eve_bit = measure_qubit(
        bit,
        alice_basis,
        eve_basis
    )

    return eve_bit