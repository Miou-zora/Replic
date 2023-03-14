#!/usr/bin/env python3
##
## @VyOkPROJECT, 2023
## mirror-generator
## File description:
## add_to_collaborators - Add collaborators to the mirror repository on Github
##

from github import Github, AuthenticatedUser, Organization, GithubException

def add_collaborators(github_usernames, repo_name, github: Github) -> None:
    user = github.get_user()
    repo = user.get_repo(repo_name)
    if type(github_usernames) != list:
        return
    for username in github_usernames:
        try:
            user = github.get_user(username)
        except GithubException as err:
            raise Exception(f"User {username} does not exist")
        repo.add_to_collaborators(user, "push")
