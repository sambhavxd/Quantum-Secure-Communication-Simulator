import numpy as np

def summarize_results(qber_list):

    return {
        "mean": np.mean(qber_list),
        "std": np.std(qber_list),
        "min": np.min(qber_list),
        "max": np.max(qber_list)
    }