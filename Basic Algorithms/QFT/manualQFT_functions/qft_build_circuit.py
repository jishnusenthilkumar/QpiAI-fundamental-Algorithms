# manual_qft/qft_build_circuit.py
from qiskit import QuantumCircuit
from .qft_core import manual_qft

def build_qft_circuit(n_qubits: int) -> QuantumCircuit:
    """
    Full QFT algorithm ready for simulation:
      • builds manual_qft
      • appends save_statevector for inspection
      • adds measurement on every qubit
    """
    qc = manual_qft(n_qubits)
    qc.save_statevector()
    qc.measure_all()
    return qc
