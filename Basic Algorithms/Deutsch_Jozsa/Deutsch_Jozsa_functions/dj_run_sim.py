# deutsch_jozsa/dj_run_sim.py
from qiskit import transpile
from qiskit_aer import AerSimulator
from .dj_build_circuit import build_dj_circuit

def run_dj(n: int, oracle_type: str = "balanced", shots: int = 1024):
    """
    Build, transpile and simulate the Deutsch–Jozsa circuit.

    Returns
    -------
    counts  : Dict[str, int]    measurement results
    circuit : QuantumCircuit    compiled circuit (unmeasured)
    """
    circuit   = build_dj_circuit(n, oracle_type)
    simulator = AerSimulator()
    compiled  = transpile(circuit, simulator)
    counts    = simulator.run(compiled, shots=shots).result().get_counts()
    return counts, circuit
