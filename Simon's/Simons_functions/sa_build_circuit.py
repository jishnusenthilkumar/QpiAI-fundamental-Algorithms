# simons_algorithm/sa_build_circuit.py
from qiskit import QuantumCircuit
from .sa_oracle import simon_oracle

def build_simon_circuit(secret: str) -> QuantumCircuit:
    """
    Construct the full Simon circuit (quantum part only).
    """
    n = len(secret)
    qc = QuantumCircuit(2 * n, n)

    # 1 | Create uniform superposition on input qubits
    qc.h(range(n))

    # 2 | Apply the oracle
    qc.compose(simon_oracle(secret), inplace=True)

    # 3 | Hadamard transform on input qubits
    qc.h(range(n))

    # 4 | Measure input qubits
    qc.measure(range(n), range(n))
    return qc
