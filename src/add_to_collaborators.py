#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

from .Github import Github, User, Repository


def add_collaborators(github_usernames: list[str],
                      repository_name: str,
                      github: Github) -> None:
    """Add all of `github_usernames` in repo named `repo_name`

    Args:
        github_usernames (list[str]): list of github username you want to add
        repo_name (str): name of the repository where you want to add users
        github (Github): github key

    Raises:
        Exception: if username doesn't exist
    """
    user: User = github.get_user()
    repo: Repository = user.get_repo(repository_name)
    if type(github_usernames) != list:
        return
    for username in github_usernames:
        try:
            user: User = github.get_user(username)
        except Exception:
            raise Exception(f"User {username} does not exist")
        repo.add_to_collaborators(user, "push")
