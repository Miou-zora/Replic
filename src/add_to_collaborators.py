#!/usr/bin/env python3
##
## @VyOkPROJECT, 2023
## mirror-generator
## File description:
## add_to_collaborators - Add collaborators to the mirror repository on Github
##

from github import Github, GithubException, AuthenticatedUser, Repository, NamedUser

def add_collaborators(github_usernames: list[str], repository_name: str, github: Github) -> None:
    """Add all of `github_usernames` in repo named `repo_name`

    Args:
        github_usernames (list[str]): list of github username you want to add
        repo_name (str): name of the repository where you want to add users
        github (Github): github key

    Raises:
        Exception: if username doesn't exist
    """
    user: AuthenticatedUser.AuthenticatedUser = github.get_user()
    repo: Repository.Repository = user.get_repo(repository_name)
    if type(github_usernames) != list:
        return
    for username in github_usernames:
        try:
            user: NamedUser.NamedUser = github.get_user(username)
        except GithubException as err:
            raise Exception(f"User {username} does not exist")
        repo.add_to_collaborators(user, "push")
