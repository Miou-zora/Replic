#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

import argparse
from collections import OrderedDict


def argumentManager():
    parser = argparse.ArgumentParser(description="A beautiful mirror-generator.")
    parser.add_argument("--friend", "-f", nargs=1, action="extend", help="Can add friend to mirror repository.")
    parser.add_argument("--mirror-name", "-m", nargs=1, help="Change the mirror repository name.")
    parser.add_argument("--commit", "-o", nargs=1, help="change the first commit push to the main repository")
    parser.add_argument("sshKey", nargs=1, help="SSH key(s) to be added to the mirror repository.")
    parser.add_argument("--input-file", "-i", nargs=1, help="Input file to be used to generate the mirror repository.")
    parsed_args = parser.parse_args()
    if parsed_args.friend:
        parsed_args.friend = list(OrderedDict.fromkeys(parsed_args.friend))
    return parsed_args
