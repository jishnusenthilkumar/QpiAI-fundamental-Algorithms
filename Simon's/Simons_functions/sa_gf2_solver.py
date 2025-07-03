# simons_algorithm/sa_gf2_solver.py
import numpy as np

def gf2_solve_simon(bitstrings: list[str], n: int) -> str:
    """
    Solve y·s = 0 (mod 2) via Gaussian elimination over GF(2) to recover 's'.

    Parameters
    ----------
    bitstrings : iterable of measurement outcomes (strings)
    n          : number of input qubits

    Returns
    -------
    str  – non-trivial solution of the homogeneous system (secret guess)
    """
    # Build matrix from non-zero bitstrings
    equations = [list(map(int, b)) for b in bitstrings if int(b, 2)]
    A = np.array(equations, dtype=int) if equations else np.zeros((0, n))

    # Forward elimination
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if A[i, c]), None)
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]          # swap
        for i in range(rows):
            if i != r and A[i, c]:
                A[i] ^= A[r]                   # XOR rows (mod 2)
        r += 1
        if r == rows:
            break

    # Extract any non-zero vector orthogonal to all rows (kernel vector)
    s = np.zeros(cols, dtype=int)
    pivots = {np.argmax(row) for row in A if row.any()}   # pivot columns
    free_cols = [c for c in range(cols) if c not in pivots]
    if free_cols:                        # set first free var to 1, back-solve
        s[free_cols[0]] = 1
        for row in reversed(A):
            if row.any():
                pivot = np.argmax(row)
                s[pivot] = row.dot(s) % 2

    return ''.join(map(str, s))
