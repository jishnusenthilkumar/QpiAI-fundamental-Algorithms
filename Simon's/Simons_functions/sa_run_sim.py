# simons_algorithm/sa_run_sim.py
from qiskit import transpile
from qiskit_aer import AerSimulator
from .sa_build_circuit import build_simon_circuit

def run_simon(secret: str, shots: int = 100):
    """
    Build, transpile, and simulate Simon’s algorithm.

    Returns
    -------
    counts  : dict[str, int]      measurement outcomes
    circuit : QuantumCircuit      the original (uncompiled) circuit
    """
    circuit   = build_simon_circuit(secret)
    simulator = AerSimulator()
    compiled  = transpile(circuit, simulator)
    counts    = simulator.run(compiled, shots=shots).result().get_counts()
    return counts, circuit
