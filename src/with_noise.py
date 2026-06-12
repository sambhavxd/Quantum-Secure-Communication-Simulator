from .measure import measure_qubit
from .noise import apply_noise

def run_with_noise(
    alice_bits,
    alice_bases,
    bob_bases,
    noise_probability=0.05
):

    bob_bits = []

    for i in range(len(alice_bits)):

        measured_bit = measure_qubit(
            alice_bits[i],
            alice_bases[i],
            bob_bases[i]
        )

        measured_bit = apply_noise(
            measured_bit,
            noise_probability
        )

        bob_bits.append(measured_bit)

    return bob_bits