# deutsch_jozsa/dj_oracle.py
from qiskit import QuantumCircuit

def deutsch_jozsa_oracle(n: int, oracle_type: str = "balanced") -> QuantumCircuit:
    """
    Build a Deutsch–Jozsa oracle.

    Parameters
    ----------
    n : int
        Number of input qubits (not counting the single output qubit).
    oracle_type : str
        'balanced'  → flips output for exactly half of the inputs.
        'constant'  → produces the same output for every input.

    Returns
    -------
    QuantumCircuit
        (n + 1)-qubit oracle circuit.
    """
    qc = QuantumCircuit(n + 1, name=f"DJ-{oracle_type}")

    if oracle_type == "constant":
        # f(x)=0  → do nothing.  (Uncomment the next two lines for f(x)=1.)
        # qc.x(n)          # put output in |1⟩
        # qc.barrier()
        pass
    elif oracle_type == "balanced":
        # Simple balanced oracle: flip output when the first input qubit is 1
        qc.cx(0, n)
    else:
        raise ValueError("oracle_type must be 'balanced' or 'constant'")

    qc.barrier()
    return qc
