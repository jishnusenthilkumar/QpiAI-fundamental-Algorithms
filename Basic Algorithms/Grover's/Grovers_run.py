# run_grover.py
from Grovers_functions.ga_run_sim     import run_grover
from Grovers_functions.ga_show_counts import show_counts

def main() -> None:
    n_data       = 3
    target_state = "101"      # must be n_data bits long

    counts, circuit = run_grover(n_data, target_state)

    print("\nGrover circuit:")
    print(circuit.draw())     # ASCII diagram in terminal

    show_counts(counts, title=f"Grover results (target = {target_state})")

if __name__ == "__main__":
    main()
