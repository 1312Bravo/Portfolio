import numpy as np
import matplotlib.pyplot as plt

def baseline_recent_weighting():
    baseline_window = 90
    recent_window = 21
    lambda_base = 0.978

    fig, ax = plt.subplots(1,2, figsize=(25,5))

    ax[0].set_title("Baseline window - Load weighting", fontsize=14)
    baseline_window_days = range(1, baseline_window+1)
    baseline_window_weights = np.array([lambda_base ** (j-1) for j in baseline_window_days])
    # baseline_window_normalized_weights = baseline_window_weights / sum(baseline_window_weights)
    ax[0].plot(np.repeat(14, 90) + baseline_window_days, baseline_window_weights, color="black", linewidth=2)
    ax[0].set_xlabel("Baseline days")


    ax[1].set_title("Recent window - Load weighting", fontsize=14)
    recent_window_days = range(1, recent_window+1)
    recent_window_weights = np.array([lambda_base ** (j-1) for j in recent_window_days])
    # recent_window_normalized_weights = recent_window_weights / sum(recent_window_weights)
    ax[1].plot(recent_window_days, recent_window_weights, color="black", linewidth=2)
    ax[1].set_xlabel("Recent days")

    for i in [0,1]:
        ax[i].set_ylim(0,1.05)
        ax[i].set_ylabel("Weight")
        ax[i].grid(alpha=0.5)

    plt.tight_layout()
    plt.show()