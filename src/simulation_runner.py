from .alice import generate_bits, generate_bases
from .bob import generate_bases as bob_generate_bases

from .no_eve import run_without_eve
from .with_eve import run_with_eve
from .with_noise import run_with_noise
from .with_eve_and_noise import run_with_eve_and_noise

from .bb84 import sift_key
from .qber import calculate_qber

def run_single_simulation(
    n=500,
    noise_probability=0.05
):

    alice_bits = generate_bits(n)
    alice_bases = generate_bases(n)

    bob_bases = bob_generate_bases(n)

    results = {}

    # No Eve
    bob_bits = run_without_eve(
        alice_bits,
        alice_bases,
        bob_bases
    )

    alice_key, bob_key = sift_key(
        alice_bits,
        alice_bases,
        bob_bits,
        bob_bases
    )

    results["No Eve"] = calculate_qber(
        alice_key,
        bob_key
    )

    # Eve
    bob_bits = run_with_eve(
        alice_bits,
        alice_bases,
        bob_bases
    )

    alice_key, bob_key = sift_key(
        alice_bits,
        alice_bases,
        bob_bits,
        bob_bases
    )

    results["Eve"] = calculate_qber(
        alice_key,
        bob_key
    )

    # Noise
    bob_bits = run_with_noise(
        alice_bits,
        alice_bases,
        bob_bases,
        noise_probability
    )

    alice_key, bob_key = sift_key(
        alice_bits,
        alice_bases,
        bob_bits,
        bob_bases
    )

    results["Noise"] = calculate_qber(
        alice_key,
        bob_key
    )

    # Eve + Noise
    bob_bits = run_with_eve_and_noise(
        alice_bits,
        alice_bases,
        bob_bases,
        noise_probability
    )

    alice_key, bob_key = sift_key(
        alice_bits,
        alice_bases,
        bob_bits,
        bob_bases
    )

    results["Eve + Noise"] = calculate_qber(
        alice_key,
        bob_key
    )

    return results