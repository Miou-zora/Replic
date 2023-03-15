#!/usr/bin/env python3
##
## @Miou-zora Project, Mirror-Generator, 2023
## push_mirror.py
## File description:
## Push to mirror_name with "CI/CD push" commit name.
##

import subprocess

def push_mirror(mirror_name: str, binary_name: str):
    actions = [(["git", "-C", f"{binary_name}/{mirror_name}/", "add", "."], "No add can be done"),
               (["git", "-C", f"{binary_name}/{mirror_name}/", "commit", "-m", "CI/CD push"], "No commit can be done"),
               (["git", "-C", f"{binary_name}/{mirror_name}/", "push"], "No push can be done")]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            raise Exception(action[1])
