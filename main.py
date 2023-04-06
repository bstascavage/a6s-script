#!/usr/local/bin/python
"""This script generates a script for A6S, to be used for callouts"""
import argparse
import time
import yaml
from termcolor import colored

# Configure argparse
parser = argparse.ArgumentParser(
    prog="SavageScripts",
    description="Generates a 'call-out' script for a raid",
)
parser.add_argument("-r", "--raid", help="Name of the raid to script")
args = parser.parse_args()


def generate_vortexer_script(raid):
    """Generates the call-out script for Vortexer in A6S"""
    print()

    input_vars = {}
    for value in raid.values():
        attrs = ["bold"] if "bold" in value and value["bold"] else ["dark"]
        color = (
            value["color"]
            if "color" in value and isinstance(value["color"], str)
            else "white"
        )

        # If line is marked as an 'input', set it as an input prompt
        # Input variables are stored to a dict
        # Variables are also encoded with green text, for better visibility
        # TODO: save variable in color and raw  # pylint: disable=W0511
        if "input" in value and value["input"]:
            input_vars[value["variable"]] = input(
                colored(value["text"], color, attrs=attrs)
            )
            input_vars[value["variable"]] = colored(
                input_vars[value["variable"]], "green", attrs=["bold"]
            )
        else:
            print(colored(value["text"].format(**input_vars), color, attrs=attrs))

        if "newline" in value and value["newline"]:
            print()

        if "sleep" in value and isinstance(value["sleep"], int):
            time.sleep(value["sleep"])


def get_raid_from_yaml(raid):
    """Gets the raid script data from a yaml file"""
    with open(f"resources/{raid}.yaml", "r", encoding="utf8") as file:
        raid_data = yaml.safe_load(file)

    return raid_data


generate_vortexer_script(get_raid_from_yaml(args.raid))
