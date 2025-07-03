# simons_algorithm/sa_oracle.py
from qiskit import QuantumCircuit

def simon_oracle(secret: str) -> QuantumCircuit:
    """
    Build Simon’s oracle for a given secret bit-string.

    The oracle encodes a 2-to-1 function f such that f(x) = f(x ⊕ s).
    """
    n = len(secret)
    qc = QuantumCircuit(2 * n, name="𝒪")

    # Example construction: wires [0..n-1] → input, [n..2n-1] → f(x)
    for i in range(n):
        qc.cx(i, n + i)          # copy input to output

    # Encode x ⊕ s dependency
    for idx, bit in enumerate(secret):
        if bit == "1":
            qc.cx(idx, n + (idx + 1) % n)   # simple shift pattern

    qc.barrier()
    return qc
