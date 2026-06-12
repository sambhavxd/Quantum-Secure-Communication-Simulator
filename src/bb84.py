def sift_key(
    alice_bits,
    alice_bases,
    bob_bits,
    bob_bases
):

    alice_key = []
    bob_key = []

    for i in range(len(alice_bits)):

        if alice_bases[i] == bob_bases[i]:

            alice_key.append(alice_bits[i])
            bob_key.append(bob_bits[i])

    return alice_key, bob_key