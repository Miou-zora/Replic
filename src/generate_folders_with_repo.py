#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

import subprocess
from .Utils.BashUtils import BashUtils


def generate_folders_with_repo(ssh_key: str,
                               project_name: str,
                               user_name: str,
                               repo_name: str,
                               mirror_name: str):
    mirror_ssh_link = f"git@github.com:{user_name}/{mirror_name}.git"
    BashUtils.mkdir(project_name)
    actions = [(["git", "clone", ssh_key],
                "Can't clone repository: " + ssh_key),
               (["mv", repo_name, project_name],
                "Can't move folder: " + repo_name),
               (["git", "clone", mirror_ssh_link],
                "Can't clone repository: " + mirror_ssh_link)]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            raise Exception(action[1])
    BashUtils.mv(mirror_name, project_name)
