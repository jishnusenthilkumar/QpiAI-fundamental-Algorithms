# manual_qft/qft_run_sim.py
from qiskit import transpile
from qiskit_aer import AerSimulator
from .qft_build_circuit import build_qft_circuit

def run_qft(n_qubits: int, shots: int = 1024):
    """
    Build, transpile and simulate the manual QFT circuit.

    Returns
    -------
    counts  : Dict[str, int]   – measurement outcomes
    circuit : QuantumCircuit   – original (uncompiled) circuit
    """
    circuit   = build_qft_circuit(n_qubits)
    simulator = AerSimulator()
    compiled  = transpile(circuit, simulator)
    counts    = simulator.run(compiled, shots=shots).result().get_counts()
    return counts, circuit
