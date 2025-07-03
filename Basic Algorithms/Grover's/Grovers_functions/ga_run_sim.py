# grover_algorithm/ga_run_sim.py
from qiskit import transpile
from qiskit_aer import AerSimulator
from .ga_build_circuit import build_grover_circuit

def run_grover(n_data: int,
               target_state: str,
               shots: int = 1024,
               n_iterations: int | None = None):
    """
    Build, transpile and simulate Grover's algorithm.

    Returns
    -------
    counts  : dict[str, int]   measurement results
    circuit : QuantumCircuit   uncompiled Grover circuit
    """
    circuit   = build_grover_circuit(n_data, target_state, n_iterations)
    simulator = AerSimulator()
    compiled  = transpile(circuit, simulator)
    counts    = simulator.run(compiled, shots=shots).result().get_counts()
    return counts, circuit
