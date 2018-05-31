#! /usr/bin/env python3

"""This is the main file for the client part of the native brightness
controller. It aims to communicate with the its server counterpart to
adjust the brightness of the screen.
"""

import argparse
import sys
import zerorpc

import config


INPUT = [
    "reset",
    "increase",
    "decrease"
]


if __name__ == "__main__":

    # Argument parsing
    PARSER = argparse.ArgumentParser(
        description="Client part of the native backlight utility.")
    PARSER.add_argument(
        'action',
        metavar='ACTION',
        type=str,
        choices=INPUT,
        nargs=1,
        help='the action to perform. Supported: increase, decrease, reset')
    ARGS = PARSER.parse_args()

    # ZeroRPC
    CLIENT = zerorpc.Client()
    ADDRESS = ("tcp://127.0.0.1:%s") % (config.communication_port())
    CLIENT.connect(ADDRESS)

    try:
        CHOICE = str(*ARGS.action)
        if CHOICE == "reset":
            CLIENT.reset()
        elif CHOICE == "decrease":
            CLIENT.decrease()
        elif CHOICE == "increase":
            CLIENT.increase()
        else:
            raise Exception(
                ("Invalid input paramater. Actual: %s, Expected: one of %s") %
                (ARGS.action, INPUT))
    except Exception as exp:
        sys.exit(exp)
