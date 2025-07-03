from qiskit import transpile
from qiskit_aer import AerSimulator
from .BV_BuildCircuit import build_bv_circuit   # ← relative import

def run_bv(secret_string: str, shots: int = 1024):
    circuit   = build_bv_circuit(secret_string)
    simulator = AerSimulator()
    compiled  = transpile(circuit, simulator)
    counts    = simulator.run(compiled, shots=shots).result().get_counts()
    return counts, circuit

