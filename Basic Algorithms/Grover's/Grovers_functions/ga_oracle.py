# grover_algorithm/ga_oracle.py
from qiskit import QuantumCircuit

def grover_oracle(n_data: int, target_state: str) -> QuantumCircuit:
    """
    Build a Grover oracle that marks the chosen |target_state⟩.

    Parameters
    ----------
    n_data : int
        Number of data qubits.
    target_state : str
        Binary string of length n_data representing the marked state.

    Returns
    -------
    QuantumCircuit
        Oracle acting on (n_data + 2) qubits (data + 2 ancilla).
    """
    if len(target_state) != n_data:
        raise ValueError("target_state length must equal n_data.")

    n_total = n_data + 2              # two ancilla qubits
    qc = QuantumCircuit(n_total, name="𝒪")

    # Flip qubits whose target bit is 0
    for idx, bit in enumerate(target_state):
        if bit == "0":
            qc.x(idx)

    # Multi-controlled X with one ancilla as target and one as work
    qc.mcx(control_qubits=list(range(n_data)),
           target_qubit=n_data,
           ancilla_qubits=[n_data + 1],
           mode="recursion")

    # Uncompute the X gates
    for idx, bit in enumerate(target_state):
        if bit == "0":
            qc.x(idx)

    qc.barrier()
    return qc
