# run_simons.py
from Simons_functions.sa_run_sim     import run_simon
from Simons_functions.sa_gf2_solver  import gf2_solve_simon
from Simons_functions.sa_show_counts import show_counts

def main() -> None:
    secret = "110"             # <-- change freely
    n      = len(secret)

    counts, circuit = run_simon(secret)

    print("\nSimon’s algorithm circuit:")
    print(circuit.draw())

    show_counts(counts, title="Simon measurement distribution")

    # Classical post-processing
    secret_guess = gf2_solve_simon(list(counts.keys()), n)
    print(f"\nRecovered secret: {secret_guess}")
    print(f"Actual secret   : {secret}")
    print("Match:", secret_guess == secret)

if __name__ == "__main__":
    main()
