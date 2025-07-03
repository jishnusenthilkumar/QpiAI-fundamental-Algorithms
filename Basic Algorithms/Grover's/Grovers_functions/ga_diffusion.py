# grover_algorithm/ga_diffusion.py
from qiskit import QuantumCircuit

def grover_diffusion(n_data: int) -> QuantumCircuit:
    """
    Standard Grover diffusion (inversion about the mean).

    Operates on (n_data + 2) qubits, re-using the same ancilla layout
    as the oracle.
    """
    n_total = n_data + 2
    qc = QuantumCircuit(n_total, name="D")

    # H·X on data qubits
    for q in range(n_data):
        qc.h(q)
        qc.x(q)

    # Multi-controlled Z using ancilla pair (implemented as X-gate sandwich)
    qc.mcx(control_qubits=list(range(n_data)),
           target_qubit=n_data,
           ancilla_qubits=[n_data + 1],
           mode="recursion")

    # X·H on data qubits
    for q in range(n_data):
        qc.x(q)
        qc.h(q)

    qc.barrier()
    return qc
