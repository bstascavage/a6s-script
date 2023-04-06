#!/usr/local/bin/python
"""This script generates a script for A6S, to be used for callouts"""
import time
from termcolor import colored


def generate_vortexer_script():
    """Generates the call-out script for Vortexer in A6S"""
    # Initial placement
    print(colored("\nEveryone stack on A\n", "white", attrs=["bold"]))

    # After first Compressed Elementals
    first_water = input(colored("First water debuff? ", "white", attrs=["dark"]))
    print(
        colored(f"The first water debuff is: {first_water}\n", "white", attrs=["dark"])
    )

    # Waiting on the first elemenal swap
    print(colored("Waiting for first Element Swap\n", "white", attrs=["dark"]))
    time.sleep(10)

    # After first elemental swap
    second_water = input(colored("Second water debuff? ", "white", attrs=["dark"]))
    print(
        colored(
            f"The second water debuff is: {second_water}\n", "white", attrs=["dark"]
        )
    )
    print(colored(f"Panic and {first_water} on A", "white", attrs=["bold"]))
    print(colored("Everyone else, stack south of the boss\n", "white", attrs=["bold"]))

    # Waiting on the second elemental swap.  Swaps every 20s but sleeping for 10s to allow for error
    print(colored("Waiting for second Element Swap\n", "white", attrs=["dark"]))
    time.sleep(10)
    print(
        colored(
            f"Element Swap! Everyone but {first_water} stack at 3",
            "white",
            attrs=["bold"],
        )
    )

    print(colored("After swap, everyone stack north of boss", "white", attrs=["bold"]))
    print(colored("Spread after AOEs\n", "white", attrs=["bold"]))

    # After Fire AOEs
    time.sleep(5)
    print(colored("After second fire AOEs", "white", attrs=["dark"]))
    print(
        colored(
            f"Spread for beams. {first_water} and {second_water} goes NW of boss.",
            "white",
            attrs=["bold"],
        )
    )
    print(
        colored("Everyone else goes south of boss after beams", "white", attrs=["bold"])
    )


generate_vortexer_script()
