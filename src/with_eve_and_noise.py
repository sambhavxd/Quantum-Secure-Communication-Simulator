from .eve import generate_eve_basis
from .eve_attack import eve_intercept

from .measure import measure_qubit
from .noise import apply_noise

def run_with_eve_and_noise(
    alice_bits,
    alice_bases,
    bob_bases,
    noise_probability=0.05
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

        bob_bit = apply_noise(
            bob_bit,
            noise_probability
        )

        bob_bits.append(bob_bit)

    return bob_bits