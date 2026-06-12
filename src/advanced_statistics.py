import matplotlib.pyplot as plt
import numpy as np

def plot_qber_distribution(qber_data):

    plt.figure(figsize=(10, 6))

    for scenario, values in qber_data.items():

        plt.hist(
            np.array(values) * 100,
            bins=20,
            alpha=0.6,
            label=scenario
        )

    plt.xlabel("QBER (%)")
    plt.ylabel("Frequency")

    plt.title(
        "Distribution of QBER Across Multiple Simulations"
    )

    plt.legend()

    plt.grid(True)

    plt.savefig(
        "qber_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()