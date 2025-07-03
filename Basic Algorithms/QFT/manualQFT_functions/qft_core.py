# manual_qft/qft_core.py
from qiskit import QuantumCircuit
import numpy as np

def manual_qft(n_qubits: int) -> QuantumCircuit:
    """
    Construct an n-qubit Quantum Fourier Transform (little-endian order).

    Returns
    -------
    QuantumCircuit  –  an n-qubit QFT without measurement.
    """
    qc = QuantumCircuit(n_qubits, name="QFT")
    pi = np.pi

    # Core QFT
    for k in range(n_qubits):
        qc.h(k)
        for j in range(k + 1, n_qubits):
            qc.cp(pi / 2 ** (j - k), j, k)

    # End-swap to reverse qubit order
    for k in range(n_qubits // 2):
        qc.swap(k, n_qubits - k - 1)

    return qc
