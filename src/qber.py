def calculate_qber(alice_key, bob_key):

    errors = 0

    for a, b in zip(alice_key, bob_key):

        if a != b:
            errors += 1

    if len(alice_key) == 0:
        return 0

    return errors / len(alice_key)