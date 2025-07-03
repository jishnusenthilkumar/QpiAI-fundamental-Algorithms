# main.py
# ────────────────────────────────────────────────────────────────
#  Entry point for the refactored Bernstein–Vazirani workflow.
#  Make sure this file sits one directory ABOVE the
#  `Bernstein_Vazirani/` package (see layout below).
# ────────────────────────────────────────────────────────────────

from Bernstein_Vazirani.BV_RunSim    import run_bv
from Bernstein_Vazirani.BV_ShowCounts import show_counts


def main() -> None:
    """Run the Bernstein_Vazirani algorithm end-to-end."""
    SECRET = "100"                           # hidden bit-string

    # 1. build, transpile and simulate
    counts, circuit = run_bv(SECRET)

    # 2. show circuit in the terminal
    print("\nBernstein–Vazirani circuit:")
    print(circuit.draw())                    # ASCII diagram

    # 3. visualise the measurement statistics
    show_counts(counts, title=f"BV results (secret = {SECRET})")


if __name__ == "__main__":
    main()

