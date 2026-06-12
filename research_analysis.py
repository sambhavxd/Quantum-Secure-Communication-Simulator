from src.simulation_runner import run_single_simulation
from src.statistics import summarize_results
from src.advanced_statistics import plot_qber_distribution

# ==========================================
# PARAMETERS
# ==========================================

runs = 100       
threshold = 0.11

# ==========================================
# DATA STORAGE
# ==========================================

qber_data = {
    "No Eve": [],
    "Eve": [],
    "Noise": [],
    "Eve + Noise": []
}

# ==========================================
# RUN SIMULATIONS
# ==========================================

for i in range(runs):

    print(f"Running Simulation {i+1}/{runs}")

    results = run_single_simulation()

    for scenario in qber_data:

        qber_data[scenario].append(
            results[scenario]
        )

# ==========================================
# STATISTICAL ANALYSIS
# ==========================================

print("\n====================================")
print("      RESEARCH ANALYSIS")
print("====================================")

for scenario in qber_data:

    stats = summarize_results(
        qber_data[scenario]
    )

    print(f"\n{scenario}")

    print(
        f"Mean QBER: "
        f"{stats['mean']*100:.2f}%"
    )

    print(
        f"Std Dev: "
        f"{stats['std']*100:.2f}%"
    )

    print(
        f"Min QBER: "
        f"{stats['min']*100:.2f}%"
    )

    print(
        f"Max QBER: "
        f"{stats['max']*100:.2f}%"
    )

# ==========================================
# EVE DETECTION RATE
# ==========================================

eve_detection_count = 0

for qber in qber_data["Eve"]:

    if qber > threshold:

        eve_detection_count += 1

eve_detection_rate = (
    eve_detection_count /
    len(qber_data["Eve"])
) * 100

print("\n====================================")
print("      ATTACK DETECTION")
print("====================================")

print(
    f"\nDetection Threshold: "
    f"{threshold*100:.1f}%"
)

print(
    f"Eve Detection Rate: "
    f"{eve_detection_rate:.2f}%"
)

# ==========================================
# SUMMARY TABLE
# ==========================================

print("\n====================================")
print("           SUMMARY")
print("====================================")

for scenario in qber_data:

    avg_qber = (
        sum(qber_data[scenario])
        / len(qber_data[scenario])
    ) * 100

    print(
        f"{scenario:<15}: "
        f"{avg_qber:.2f}%"
    )

# ==========================================
# VISUALIZATION
# ==========================================

plot_qber_distribution(
    qber_data
)