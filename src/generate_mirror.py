#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

from .Github.Github import Github
from sys import *
import os


def generate_mirror(orga_name: str, repo_name: str, github: Github, mirror_name: str, projects: list[str] = None):
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
    except Exception as err:
        try:
            mirror = user.create_repo(
                mirror_name,
                allow_rebase_merge=True,
                auto_init=False,
                has_issues=True,
                has_projects=(projects is not None),
                has_wiki=False,
                private=True,
            )
        except Exception as err:
            raise Exception(f"ERROR: generate_mirror: Unable to create mirror repository: {err.data['errors'][0]['message']}")
        f = open(os.path.expanduser('~') + "/.ssh/id_rsa", "r")
        private_key = f.read()
        f.close()
        repo.create_secret("GIT_SSH_PRIVATE_KEY", private_key)
        if projects:
            for project_name in projects:
                mirror.create_project(project_name)
        return
    raise Exception("ERROR: generate_mirror: Mirror already exists")
