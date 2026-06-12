from .measure import measure_qubit

def run_without_eve(
    alice_bits,
    alice_bases,
    bob_bases
):

    bob_bits = []

    for i in range(len(alice_bits)):

        bob_bit = measure_qubit(
            alice_bits[i],
            alice_bases[i],
            bob_bases[i]
        )

        bob_bits.append(bob_bit)

    return bob_bits