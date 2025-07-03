# manual_qft/qft_show_counts.py
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def show_counts(counts: dict, title: str = ""):
    """
    Display a histogram of measurement results. Returns the Matplotlib figure.
    """
    fig = plot_histogram(counts, title=title)
    fig.tight_layout()
    plt.show()
    return fig
