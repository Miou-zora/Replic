#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

import subprocess


def push_mirror(mirror_name: str, project_name: str, commit: str):
    actions = [(["git", "-C", f"{project_name}/{mirror_name}/", "add", "."],
                "No add can be done"),
               (["git", "-C", f"{project_name}/{mirror_name}/", "commit",
                 "-m", commit], "No commit can be done"),
               (["git", "-C", f"{project_name}/{mirror_name}/", "push"],
                "No push can be done")]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            raise Exception(action[1])
