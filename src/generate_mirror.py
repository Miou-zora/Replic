#!/usr/bin/env python3
##
## @Miou-zora Project, Mirror-Generator, 2023
## generate_mirror.py
## File description:
## Create the mirror of `repo_name` of `orga_name` where `orga_name` is epitech organization and `repo_name` the name of the repository in organization.
## The mirror is named [repo_name]-mirror.
##

from .Github.Github import Github
from sys import *
import os

def generate_mirror(orga_name: str, repo_name: str, github: Github, mirror_name: str):
    try:
        orga = github.get_organization(orga_name)
    except Exception as err:
        raise Exception("ERROR: generate_mirror: Unable to find organization" + str(err))
    try:
        repo = orga.get_repo(repo_name)
    except Exception as err:
        raise Exception("ERROR: generate_mirror: Unable to find repository")
    user = github.get_user()
    try:
        user.get_repo(mirror_name)
        raise Exception("ERROR: generate_mirror: Mirror already exists")
    except:
        try:
            user.create_repo(
                mirror_name,
                allow_rebase_merge=True,
                auto_init=False,
                has_issues=True,
                has_projects=False,
                has_wiki=False,
                private=True,
            )
        except Exception as err:
            raise Exception(f"ERROR: generate_mirror: Unable to create mirror repository: {err.data['errors'][0]['message']}")
    repo = user.get_repo(mirror_name)
    f = open(os.path.expanduser('~') + "/.ssh/id_rsa", "r")
    private_key = f.read()
    f.close()
    repo.create_secret("GIT_SSH_PRIVATE_KEY", private_key)
