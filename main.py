#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## mirror-generator
## File description:
## test
##

from github import Github, AuthenticatedUser, Organization, GithubException
from sys import argv
import json
import subprocess
import os

def generateMirror(orgaName: str, repoName: str, github: Github):
    try:
        orga = github.get_organization(orgaName)
    except GithubException as err:
        print("Organization not found:", err)
        return
    try:
        repo = orga.get_repo(repoName)
    except GithubException as err:
        print("Repository not found:", err)
        return
    user = github.get_user()
    mirrorName = repoName + "-mirror"
    try:
        user.get_repo(mirrorName)
        print("Mirror already exist:", mirrorName)
        return
    except:
        user.create_repo(
            mirrorName,
            allow_rebase_merge=True,
            auto_init=False,
            has_issues=True,
            has_projects=False,
            has_wiki=False,
            private=True,
        )
    repo = user.get_repo(mirrorName)
    f = open(os.path.expanduser('~') + "/.ssh/id_rsa", "r")
    private_key = f.read()
    f.close()
    repo.create_secret("GIT_SSH_PRIVATE_KEY", private_key)

def generateFoldersWithRepo(repoSshLink: str, userName: str, repoName: str):
    mirrorSshLink = f"git@github.com:{userName}/{repoName}-mirror.git"
    mirrorName = f"{repoName}-mirror"
    projectName = repoSshLink.split('-')[-2]
    actions = [(["mkdir", projectName], "Folder already exist: " + projectName),
               (["git", "clone", repoSshLink], "Can't clone repository: " + repoSshLink),
               (["mv", repoName, projectName], "Can't move folder: " + repoName),
               (["git", "clone", mirrorSshLink], "Can't clone repository: " + mirrorSshLink),
               (["mv", mirrorName, projectName], "Can't move folder: " + mirrorName)]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            print(action[1])
            return

def generateMirrorWorkflow(binaryName: str, repoSsh: str, repoName:str):
    mirrorName = f"{repoName}-mirror"
    f = open("verif_mirror.yml", "r")
    file = f.read()
    f.close()
    file = file.replace("MIRROR_URL_MIRROR_GENERATOR", repoSsh)
    file = file.replace("EXECUTABLE_MIRROR_GENERATOR", binaryName)
    actions = [(["mkdir", f"{binaryName}/{mirrorName}/.github"], "Folder already exist: " + f"{binaryName}/{mirrorName}/.github"),
               (["mkdir", f"{binaryName}/{mirrorName}/.github/workflows"], "Folder already exist: " + f"{binaryName}/{mirrorName}/.github/workflows")]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            print(action[1])
            return
    mirror_file = open(f"{binaryName}/{mirrorName}/.github/workflows/verif_mirror.yml", "w")
    mirror_file.write(file)
    mirror_file.close()

def pushMirror(mirrorName: str, binaryName: str):
    actions = [(["git", "-C", f"{binaryName}/{mirrorName}/", "add", "."], "No add can be done"),
               (["git", "-C", f"{binaryName}/{mirrorName}/", "commit", "-m", "CI/CD push"], "No commit can be done"),
               (["git", "-C", f"{binaryName}/{mirrorName}/", "push"], "No push can be done")]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            print(action[1])
            return

def main():
    if len(argv) != 2:
        exit(84)
    repo_info = argv[1].split(":")[1].split("/")
    file = json.load(open("data.json"))

    github_identifier: Github = Github(file["token"])
    orgaName = repo_info[0]
    repoName = ".".join(repo_info[1].split(".")[:-1])
    generateMirror(orgaName, repoName, github_identifier)
    generateFoldersWithRepo(argv[1], github_identifier.get_user().login, repoName)
    generateMirrorWorkflow(argv[1].split('-')[-2], argv[1], repoName)
    pushMirror(f"{repoName}-mirror", argv[1].split('-')[-2])

if __name__ == '__main__':
    main()
