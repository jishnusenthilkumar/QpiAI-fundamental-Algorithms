# run_dj.py
from Deutsch_Jozsa_functions.dj_run_sim     import run_dj
from Deutsch_Jozsa_functions.dj_show_counts import show_counts

def main() -> None:
    n          = 4           # number of input qubits
    oracle_typ = "constant"  # 'balanced' or 'constant'

    counts, circuit = run_dj(n, oracle_typ)

    print("\nDeutsch–Jozsa circuit:")
    print(circuit.draw())    # ASCII diagram in terminal

    show_counts(counts, title=f"DJ results (oracle = {oracle_typ})")

if __name__ == "__main__":
    main()
