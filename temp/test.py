#!/usr/bin/env python3
from github import Github, AuthenticatedUser, Organization, GithubException
from sys import argv
import json
import subprocess

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

def generateFoldersWithRepo(repoSshLink: str, userName: str):
    repoName = repoSshLink.split("/")[1][:-4]
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

def main():
    if len(argv) != 2:
        exit(84)
    repo_info = argv[1].split(":")[1].split("/")
    file = json.load(open("data.json"))

    github_identifier = Github(file["token"])
    orgaName = repo_info[0]
    repoName = ".".join(repo_info[1].split(".")[:-1])
    # generateMirror(orgaName, repoName, github_identifier)
    generateFoldersWithRepo(argv[1], github_identifier.get_user().login)

    # generateMirror(user, orga, )
    # orga = github_identifier.get_organization(repo_info[0])
    # user = github_identifier.get_user()
    # print(orga.get_repo(".".join(repo_info[1].split(".")[:-1])))
    # main_folder = repo_info[1].split('-')[-2]
    # subprocess.run(["mkdir", main_folder])
    # subprocess.run(["git", "clone", argv[1]])
    # subprocess.run(["mv", ".".join(repo_info[1].split(".")[:-1]), main_folder])
    # print(organizations.get_ get_repo(argv[1]))
    # organizations.create_repo(
    #     "testmirror",
    #     allow_rebase_merge=True,
    #     auto_init=False,
    #     description="ades",
    #     has_issues=True,
    #     has_projects=False,
    #     has_wiki=False,
    #     private=True,
    # )

if __name__ == '__main__':
    main()
