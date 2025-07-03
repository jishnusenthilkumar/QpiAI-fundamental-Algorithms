# run_qft.py
from manualQFT_functions.qft_run_sim     import run_qft
from manualQFT_functions.qft_show_counts import show_counts

def main() -> None:
    n_qubits = 5                      # change as needed
    counts, circuit = run_qft(n_qubits)

    print("\nManual QFT circuit:")
    print(circuit.draw())             # ASCII diagram in terminal

    show_counts(counts, title=f"Manual QFT – {n_qubits} qubits")

if __name__ == "__main__":
    main()
