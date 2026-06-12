from .alice import generate_bits
from .alice import generate_bases

from .bob import generate_bases as bob_generate_bases

from .with_real_noise import run_with_real_noise

from .bb84 import sift_key
from .qber import calculate_qber

n = 1000

alice_bits = generate_bits(n)
alice_bases = generate_bases(n)

bob_bases = bob_generate_bases(n)

bob_bits = run_with_real_noise(
    alice_bits,
    alice_bases,
    bob_bases,
    0.05
)

alice_key, bob_key = sift_key(
    alice_bits,
    alice_bases,
    bob_bits,
    bob_bases
)

qber = calculate_qber(
    alice_key,
    bob_key
)

print(
    f"Real Quantum Noise QBER: {qber*100:.2f}%"
)