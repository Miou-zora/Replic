#!/usr/bin/env python3
##
## @VyOkPROJECT, 2023
## mirror-generator
## File description:
## argument manager it's parser for arguments and return it to main
##

import argparse

def argumentManager():
    parser = argparse.ArgumentParser(description="A beautiful mirror-generator.")
    parser.add_argument("--friend", "-f", nargs=1, action="extend", help="Can add friend to mirror repository")
    parser.add_argument("sshKey", nargs="+", help="SSH key(s) to be added to the mirror repository")
    if not parser.parse_args().sshKey:
        parser.error("arg > 2 is required")
    return parser.parse_args()
