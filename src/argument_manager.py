#!/usr/bin/env python3
##
## @Miou-zora Project, Mirror-Generator, 2023
## argument_manager.py
## File description:
## Parse argument depending on flags like `-f`.
##

import argparse

def argumentManager():
    parser = argparse.ArgumentParser(description="A beautiful mirror-generator.")
    parser.add_argument("--friend", "-f", nargs=1, action="extend", help="Can add friend to mirror repository")
    parser.add_argument("sshKey", nargs=1, help="SSH key(s) to be added to the mirror repository")
    return parser.parse_args()
