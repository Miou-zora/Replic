#!/usr/bin/env python3
##
## @Miou-zora PROJECT, 2023
## mirror-generator
## File description:
## why do you look at this aweful code ...
##

from github import Github, AuthenticatedUser, Organization, GithubException
from sys import argv
import json
import subprocess
import os

def generate_mirror(orga_name: str, repo_name: str, github: Github):
    try:
        orga = github.get_organization(orga_name)
    except GithubException as err:
        print("Organization not found:", err)
        exit(84)
    try:
        repo = orga.get_repo(repo_name)
    except GithubException as err:
        print("Repository not found:", err)
        exit(84)
    user = github.get_user()
    mirror_name = repo_name + "-mirror"
    try:
        user.get_repo(mirror_name)
        print("Mirror already exist:", mirror_name)
        exit(84)
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
    f = open(os.path.expanduser('~') + "/.ssh/id_rsa", "r")
    private_key = f.read()
    f.close()
    repo.create_secret("GIT_SSH_PRIVATE_KEY", private_key)

def generate_folders_with_repo(repo_ssh_link: str, user_name: str, repo_name: str):
    mirror_ssh_link = f"git@github.com:{user_name}/{repo_name}-mirror.git"
    mirror_name = f"{repo_name}-mirror"
    project_name = repo_ssh_link.split('-')[-2]
    actions = [(["mkdir", project_name], "Folder already exist: " + project_name),
               (["git", "clone", repo_ssh_link], "Can't clone repository: " + repo_ssh_link),
               (["mv", repo_name, project_name], "Can't move folder: " + repo_name),
               (["git", "clone", mirror_ssh_link], "Can't clone repository: " + mirror_ssh_link),
               (["mv", mirror_name, project_name], "Can't move folder: " + mirror_name)]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            print(action[1])
            exit(84)

def generate_mirror_workflow(binary_name: str, repo_ssh: str, repo_name:str):
    mirror_name = f"{repo_name}-mirror"
    f = open("verif_mirror.yml", "r")
    mirror_file_data = f.read()
    f.close()
    mirror_file_data = mirror_file_data.replace("MIRROR_URL_MIRROR_GENERATOR", repo_ssh)
    mirror_file_data = mirror_file_data.replace("EXECUTABLE_MIRROR_GENERATOR", binary_name)
    actions = [(["mkdir", f"{binary_name}/{mirror_name}/.github"], "Folder already exist: " + f"{binary_name}/{mirror_name}/.github"),
               (["mkdir", f"{binary_name}/{mirror_name}/.github/workflows"], "Folder already exist: " + f"{binary_name}/{mirror_name}/.github/workflows")]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            print(action[1])
            exit(84)
    mirror_file = open(f"{binary_name}/{mirror_name}/.github/workflows/verif_mirror.yml", "w")
    mirror_file.write(mirror_file_data)
    mirror_file.close()

def push_mirror(mirror_name: str, binary_name: str):
    actions = [(["git", "-C", f"{binary_name}/{mirror_name}/", "add", "."], "No add can be done"),
               (["git", "-C", f"{binary_name}/{mirror_name}/", "commit", "-m", "CI/CD push"], "No commit can be done"),
               (["git", "-C", f"{binary_name}/{mirror_name}/", "push"], "No push can be done")]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            print(action[1])
            exit(84)

def add_collaborators(github_usernames: list, repo_name: str, github: Github):
    user = github.get_user()
    repo = user.get_repo(repo_name)
    for github_username in github_usernames:
        repo.add_to_collaborators(github_username[0], permission="push")

def main():
    if len(argv) <= 2:
        exit(84)
    github_usernames = []
    i = 1
    while i < len(argv):
        arg = argv[i]
        if arg == "--friend":
            github_usernames.append(argv[i + 1:len(argv) - 1])
            i += len(argv) - 1
    repo_info = argv[len(argv) - 1].split(":")[1].split("/")
    json_file = json.load(open("data.json"))
    github_identifier: Github = Github(json_file["token"])
    orga_name = repo_info[0]
    repo_name = ".".join(repo_info[1].split(".")[:-1])
    generate_mirror(orga_name, repo_name, github_identifier)
    generate_folders_with_repo(argv[len(argv) - 1], github_identifier.get_user().login, repo_name)
    generate_mirror_workflow(argv[len(argv) - 1].split('-')[-2], argv[len(argv) - 1], repo_name)
    add_collaborators(github_usernames, f"{repo_name}-mirror", github_identifier)
    push_mirror(f"{repo_name}-mirror", argv[len(argv) - 1].split('-')[-2])

if __name__ == '__main__':
    main()
