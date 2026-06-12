from src.alice import generate_bits, generate_bases
from src.bob import generate_bases as bob_generate_bases

from src.no_eve import run_without_eve
from src.with_eve import run_with_eve
from src.with_noise import run_with_noise
from src.with_eve_and_noise import run_with_eve_and_noise

from src.bb84 import sift_key
from src.qber import calculate_qber
from src.detection import detect_attack

from src.visualization import plot_qber

# ==========================================
# PARAMETERS
# ==========================================

n = 1000
noise_probability = 0.05

# ==========================================
# ALICE & BOB SETUP
# ==========================================

alice_bits = generate_bits(n)
alice_bases = generate_bases(n)

bob_bases = bob_generate_bases(n)

# ==========================================
# WITHOUT EVE
# ==========================================

bob_bits_no_eve = run_without_eve(
    alice_bits,
    alice_bases,
    bob_bases
)

alice_key_no_eve, bob_key_no_eve = sift_key(
    alice_bits,
    alice_bases,
    bob_bits_no_eve,
    bob_bases
)

qber_no_eve = calculate_qber(
    alice_key_no_eve,
    bob_key_no_eve
)

# ==========================================
# WITH EVE
# ==========================================

bob_bits_eve = run_with_eve(
    alice_bits,
    alice_bases,
    bob_bases
)

alice_key_eve, bob_key_eve = sift_key(
    alice_bits,
    alice_bases,
    bob_bits_eve,
    bob_bases
)

qber_eve = calculate_qber(
    alice_key_eve,
    bob_key_eve
)

# ==========================================
# NOISE ONLY
# ==========================================

bob_bits_noise = run_with_noise(
    alice_bits,
    alice_bases,
    bob_bases,
    noise_probability
)

alice_key_noise, bob_key_noise = sift_key(
    alice_bits,
    alice_bases,
    bob_bits_noise,
    bob_bases
)

qber_noise = calculate_qber(
    alice_key_noise,
    bob_key_noise
)

# ==========================================
# EVE + NOISE
# ==========================================

bob_bits_eve_noise = run_with_eve_and_noise(
    alice_bits,
    alice_bases,
    bob_bases,
    noise_probability
)

alice_key_eve_noise, bob_key_eve_noise = sift_key(
    alice_bits,
    alice_bases,
    bob_bits_eve_noise,
    bob_bases
)

qber_eve_noise = calculate_qber(
    alice_key_eve_noise,
    bob_key_eve_noise
)

# ==========================================
# RESULTS
# ==========================================

print("\n======================================")
print("      BB84 SECURITY ANALYSIS")
print("======================================")

print("\n[1] WITHOUT EVE")
print("Key Length:", len(alice_key_no_eve))
print("QBER:", round(qber_no_eve * 100, 2), "%")
print("Attack Detected:", detect_attack(qber_no_eve))

print("\n[2] WITH EVE")
print("Key Length:", len(alice_key_eve))
print("QBER:", round(qber_eve * 100, 2), "%")
print("Attack Detected:", detect_attack(qber_eve))

print("\n[3] NOISE ONLY")
print("Key Length:", len(alice_key_noise))
print("QBER:", round(qber_noise * 100, 2), "%")
print("Attack Detected:", detect_attack(qber_noise))

print("\n[4] EVE + NOISE")
print("Key Length:", len(alice_key_eve_noise))
print("QBER:", round(qber_eve_noise * 100, 2), "%")
print("Attack Detected:", detect_attack(qber_eve_noise))

print("\n======================================")
print("              SUMMARY")
print("======================================")

print(f"No Eve       : {round(qber_no_eve * 100, 2)} %")
print(f"Eve          : {round(qber_eve * 100, 2)} %")
print(f"Noise        : {round(qber_noise * 100, 2)} %")
print(f"Eve + Noise  : {round(qber_eve_noise * 100, 2)} %")

# ==========================================
# VISUALIZATION
# ==========================================

plot_qber(
    qber_no_eve,
    qber_eve,
    qber_noise,
    qber_eve_noise
)