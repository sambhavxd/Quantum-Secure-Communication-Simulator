from .measure_with_noise import (
    measure_qubit_with_noise
)

def run_with_real_noise(
    alice_bits,
    alice_bases,
    bob_bases,
    noise_probability=0.05
):

    bob_bits = []

    for i in range(len(alice_bits)):

        bit = measure_qubit_with_noise(
            alice_bits[i],
            alice_bases[i],
            bob_bases[i],
            noise_probability
        )

        bob_bits.append(bit)

    return bob_bits