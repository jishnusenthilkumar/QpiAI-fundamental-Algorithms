import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def show_counts(counts: dict, title: str = ""):
    """
    Display a histogram of measurement results.

    Parameters
    ----------
    counts : dict
        Output from `run_bv` (or any Qiskit job).
    title : str, optional
        Chart title (default empty).

    Returns
    -------
    matplotlib.figure.Figure
        The histogram figure object.
    """
    fig = plot_histogram(counts, title=title)
    fig.tight_layout()
    plt.show()
    return fig
