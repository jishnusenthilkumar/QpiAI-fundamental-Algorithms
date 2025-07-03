from qiskit import QuantumCircuit

def bv_oracle(secret_string: str) -> QuantumCircuit:
    """
    Create a Bernstein–Vazirani oracle for a given secret bit-string.

    Parameters
    ----------
    secret_string : str
        Binary string (e.g., "1011") representing the hidden vector.

    Returns
    -------
    QuantumCircuit
        A circuit with (n + 1) qubits whose action is
        |x⟩|y⟩ → |x⟩|y ⊕ s·x⟩, where s is the secret string.
    """
    n = len(secret_string)
    qc = QuantumCircuit(n + 1, name="BV-oracle")
    for idx, bit in enumerate(secret_string):
        if bit == "1":
            qc.cx(idx, n)          # control = input qubit, target = output qubit
    qc.barrier()
    return qc
