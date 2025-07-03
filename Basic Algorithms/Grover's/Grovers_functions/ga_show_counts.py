# grover_algorithm/ga_show_counts.py
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def show_counts(counts: dict[str, int], title: str = ""):
    """
    Display a histogram of measurement counts.
    """
    fig = plot_histogram(counts, title=title)
    fig.tight_layout()
    plt.show()
    return fig
