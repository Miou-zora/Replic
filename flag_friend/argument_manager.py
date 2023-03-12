#!/usr/bin/env python3
##
## @VyOkPROJECT, 2023
## mirror-generator
## File description:
## why do you look at this aweful code ...
##

import argparse

def argumentManager():
    parser = argparse.ArgumentParser(description="A beautiful mirror-generator.")
    parser.add_argument("--friend", "-f", nargs="+", help="Can add friend to mirror repository")
    return parser.parse_args()
