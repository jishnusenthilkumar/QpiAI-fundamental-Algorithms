# deutsch_jozsa/dj_show_counts.py
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def show_counts(counts: dict, title: str = ""):
    """
    Render a histogram of the measurement results.
    """
    fig = plot_histogram(counts, title=title)
    fig.tight_layout()
    plt.show()
    return fig
