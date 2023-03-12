#!/usr/bin/env python3
##
## @VyOkPROJECT, 2023
## mirror-generator
## File description:
## add_to_collaborators - Add collaborators to the mirror repository on Github
##

from github import Github, AuthenticatedUser, Organization, GithubException

def add_collaborators(github_usernames, repo_name, github: Github):
    user = github.get_user()
    repo = user.get_repo(repo_name)
    for username in github_usernames:
        try:
            user = github.get_user(username)
        except GithubException as err:
            print(github_usernames)
            print("User not found:", err)
            exit(84)
        repo.add_to_collaborators(user, "push")
