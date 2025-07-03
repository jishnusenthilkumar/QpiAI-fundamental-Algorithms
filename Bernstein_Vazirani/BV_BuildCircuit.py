from qiskit import QuantumCircuit
from .BV_Oracle import bv_oracle        # ← relative import

def build_bv_circuit(secret_string: str) -> QuantumCircuit:
    n = len(secret_string)
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n + 1))
    qc.barrier()

    qc.compose(bv_oracle(secret_string), inplace=True)

    qc.h(range(n))
    qc.barrier()
    qc.measure(range(n), range(n))
    return qc

