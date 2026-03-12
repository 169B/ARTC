"""
ARTC Visualization: Truth vs Reconstructed
Plots original data against decompressed output for various test signals.
"""

import numpy as np
import matplotlib.pyplot as plt
from artc import ARTC, ARTCLITE


def run_and_plot(ax, truth: np.ndarray, title: str, compressor, label: str = "ARTC-LITE"):
    """Compress, decompress, and plot truth vs reconstructed on given axes."""
    compressed = compressor.compress(truth)
    reconstructed = compressor.decompress(compressed)

    # Trim to match lengths (in case of incomplete final block)
    n = min(len(truth), len(reconstructed))
    x = np.arange(n)

    ax.plot(x, truth[:n], "b-", label="Truth", alpha=0.8, linewidth=2)
    ax.plot(x, reconstructed[:n], "r--", label="Reconstructed", alpha=0.8, linewidth=1.5)
    ax.set_title(title)
    ax.set_xlabel("Index")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(truth.min() - 0.5, truth.max() + 0.5)

    # Add error/residual subplot or annotation
    if n > 0:
        error = np.abs(truth[:n] - reconstructed[:n])
        max_err = np.max(error)
        ax.text(
            0.02, 0.98, f"Max error: {max_err:.4f}\nRatio: {compressor.get_ratio():.1f}x",
            transform=ax.transAxes, fontsize=8, verticalalignment="top",
            bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5),
        )


def main():
    np.random.seed(42)
    n = 128  # Multiple of 8 for clean blocks

    # 1. Perfectly linear - best case for ARTC
    linear = np.linspace(20, 35, n)

    # 2. Nearly linear with small noise - good compression
    nearly_linear = 20 + 0.12 * np.arange(n, dtype=float) + np.random.normal(0, 0.03, n)

    # 3. Temperature-like (smooth curve) - partial compression
    t = np.linspace(0, 24, n)
    temperature = 20 + 5 * np.sin(2 * np.pi * t / 24) + np.random.normal(0, 0.05, n)

    # 4. Step function - poor compression (discontinuities)
    step = np.repeat([10, 20, 15, 25, 18], n // 5)[:n].astype(float)
    step = step + np.random.normal(0, 0.1, n)

    # 5. Random - no compression
    random_data = np.random.uniform(15, 30, n)

    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    axes = axes.flatten()

    # ARTC-LITE with tolerance 0.1
    lite = ARTCLITE(block_size=8, tolerance=0.1)

    run_and_plot(axes[0], linear, "1. Perfectly Linear (best case)", lite)
    lite.reset_stats()
    run_and_plot(axes[1], nearly_linear, "2. Nearly Linear + Noise", lite)
    lite.reset_stats()
    run_and_plot(axes[2], temperature, "3. Temperature Cycle", lite)
    lite.reset_stats()
    run_and_plot(axes[3], step, "4. Step Function (challenging)", lite)
    lite.reset_stats()
    run_and_plot(axes[4], random_data, "5. Random (no structure)", lite)

    # Residual plot for temperature (example)
    lite.reset_stats()
    compressed = lite.compress(temperature)
    recon = lite.decompress(compressed)
    n_trim = min(len(temperature), len(recon))
    residuals = temperature[:n_trim] - recon[:n_trim]
    axes[5].bar(np.arange(n_trim), residuals, color="steelblue", alpha=0.7, width=0.8)
    axes[5].axhline(0, color="black", linewidth=0.5)
    axes[5].axhline(lite.tolerance, color="red", linestyle="--", alpha=0.5, label=f"±tolerance ({lite.tolerance})")
    axes[5].axhline(-lite.tolerance, color="red", linestyle="--", alpha=0.5)
    axes[5].set_title("6. Residuals (Temperature)")
    axes[5].set_xlabel("Index")
    axes[5].set_ylabel("Truth − Reconstructed")
    axes[5].legend(fontsize=8)
    axes[5].grid(True, alpha=0.3)

    plt.suptitle("ARTC-LITE: Truth vs Reconstructed", fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()
    plt.savefig("artc_truth_vs_reconstructed.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Saved: artc_truth_vs_reconstructed.png")


if __name__ == "__main__":
    main()
