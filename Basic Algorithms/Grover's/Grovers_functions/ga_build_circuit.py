# grover_algorithm/ga_build_circuit.py
from qiskit import QuantumCircuit
from .ga_oracle    import grover_oracle
from .ga_diffusion import grover_diffusion

def build_grover_circuit(n_data: int,
                         target_state: str,
                         n_iterations: int | None = None) -> QuantumCircuit:
    """
    Construct the full Grover circuit (1 round by default).

    If n_iterations is None, a single Grover iteration is applied.
    """
    n_total = n_data + 2
    qc = QuantumCircuit(n_total, n_data)

    # 1) Create equal superposition on data qubits
    qc.h(range(n_data))

    # 2) Determine how many Grover iterations to run
    if n_iterations is None:
        n_iterations = 1            # for small databases, one iteration suffices

    # 3) Apply iterations
    for _ in range(n_iterations):
        qc.compose(grover_oracle(n_data, target_state),    inplace=True)
        qc.compose(grover_diffusion(n_data),               inplace=True)

    # 4) Measure the data qubits
    qc.measure(range(n_data), range(n_data))
    return qc
