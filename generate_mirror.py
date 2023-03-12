#!/usr/bin/env python3
##
## @Miou-zora PROJECT, 2023
## mirror-generator
## File description:
## why do you look at this aweful code ...
##

from github import Github, GithubException
from sys import *
import os

def generate_mirror(orga_name: str, repo_name: str, github: Github):
    try:
        orga = github.get_organization(orga_name)
    except GithubException as err:
        raise Exception("Unable to find organization")
    try:
        repo = orga.get_repo(repo_name)
    except GithubException as err:
        raise Exception("Unable to find repository")
    user = github.get_user()
    mirror_name = repo_name + "-mirror"
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
