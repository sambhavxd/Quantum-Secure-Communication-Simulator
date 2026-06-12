import matplotlib.pyplot as plt

def plot_qber(
    qber_no_eve,
    qber_eve,
    qber_noise,
    qber_eve_noise
):

    scenarios = [
        "No Eve",
        "Eve",
        "Noise",
        "Eve + Noise"
    ]

    qber_values = [
        qber_no_eve * 100,
        qber_eve * 100,
        qber_noise * 100,
        qber_eve_noise * 100
    ]

    plt.figure(figsize=(8,5))

    plt.bar(scenarios, qber_values)

    plt.ylabel("QBER (%)")
    plt.xlabel("Scenario")

    plt.title(
        "BB84 Quantum Key Distribution Security Analysis"
    )

    plt.grid(axis="y")

    plt.show()