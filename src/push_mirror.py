#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

import subprocess
from .Utils.BashUtils import BashUtils


def push_mirror(mirror_name: str, project_name: str, commit: str):
    BashUtils.Git.add(where=f"{project_name}/{mirror_name}/")
    BashUtils.Git.commit(message=commit, where=f"{project_name}/{mirror_name}/")
    BashUtils.Git.push(where=f"{project_name}/{mirror_name}/")
