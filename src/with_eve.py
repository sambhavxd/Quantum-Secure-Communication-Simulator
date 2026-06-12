from .eve import generate_eve_basis
from .eve_attack import eve_intercept

from .measure import measure_qubit

def run_with_eve(
    alice_bits,
    alice_bases,
    bob_bases
):

    bob_bits = []

    for i in range(len(alice_bits)):

        eve_basis = generate_eve_basis()

        eve_bit = eve_intercept(
            alice_bits[i],
            alice_bases[i],
            eve_basis
        )

        bob_bit = measure_qubit(
            eve_bit,
            eve_basis,
            bob_bases[i]
        )

        bob_bits.append(bob_bit)

    return bob_bits