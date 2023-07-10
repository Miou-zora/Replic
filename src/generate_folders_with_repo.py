#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

import subprocess
from .Utils.BashUtils import BashUtils


def generate_folders_with_repo(ssh_key: str, project_name: str, user_name: str, repo_name: str, mirror_name: str):
    mirror_ssh_link = f"git@github.com:{user_name}/{mirror_name}.git"
    BashUtils.mkdir(project_name)
    BashUtils.Git.clone(ssh_key)
    BashUtils.mv(repo_name, project_name)
    BashUtils.Git.clone(mirror_ssh_link)
    BashUtils.mv(mirror_name, project_name)
