#!/usr/bin/env python3
##
## @Miou-zora Project, Mirror-Generator, 2023
## generate_mirror.py
## File description:
## Create the mirror of `repo_name` of `orga_name` where `orga_name` is epitech organization and `repo_name` the name of the repository in organization.
## The mirror is named [repo_name]-mirror.
##

from github import Github, GithubException
from sys import *
import os

def generate_mirror(orga_name: str, repo_name: str, github: Github, mirror_name: str):
    try:
        orga = github.get_organization(orga_name)
    except GithubException as err:
        raise Exception("Unable to find organization")
    try:
        repo = orga.get_repo(repo_name)
    except GithubException as err:
        raise Exception("Unable to find repository")
    user = github.get_user()
    try:
        user.get_repo(mirror_name)
        raise Exception("Mirror already exists")
    except:
        user.create_repo(
            mirror_name,
            allow_rebase_merge=True,
            auto_init=False,
            has_issues=True,
            has_projects=False,
            has_wiki=False,
            private=True,
        )
    repo = user.get_repo(mirror_name)
    f = open(os.path.expanduser('~') + "/.ssh/id_rsa", "r")
    private_key = f.read()
    f.close()
    repo.create_secret("GIT_SSH_PRIVATE_KEY", private_key)
