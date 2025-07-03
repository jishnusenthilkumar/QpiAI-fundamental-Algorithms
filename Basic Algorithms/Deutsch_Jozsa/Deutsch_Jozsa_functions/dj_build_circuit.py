# deutsch_jozsa/dj_build_circuit.py
from qiskit import QuantumCircuit
from .dj_oracle import deutsch_jozsa_oracle

def build_dj_circuit(n: int, oracle_type: str = "balanced") -> QuantumCircuit:
    """
    Full Deutsch–Jozsa algorithm circuit (includes measurement).
    """
    qc = QuantumCircuit(n + 1, n)

    qc.x(n)                 # |1⟩ on output qubit
    qc.h(range(n + 1))      # Hadamards on all qubits
    qc.barrier()

    qc.compose(deutsch_jozsa_oracle(n, oracle_type), inplace=True)

    qc.h(range(n))          # Hadamards on input qubits only
    qc.barrier()
    qc.measure(range(n), range(n))

    return qc
