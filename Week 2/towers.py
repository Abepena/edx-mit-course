"""
Towers of Hanoi example
"""


def print_move(fr, to):
    print(f"move from {fr} to {to}")


def towers(n, fr, to, spare):
    """
    Move an entire stack of n discs on 3 pikes (P1, P2, P3)
    each one smaller as you go up the pike. From one 
    pike to another. The larger discs can never go over
    the smaller discs which were originally above them
    """

    if n == 1:
        print_move(fr, to)
    else:
        towers(n - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n - 1, spare, to, fr)


towers(4, "P1", "P2", "P3")
