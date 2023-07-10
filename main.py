#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

from sys import argv
import json
from src.add_to_collaborators import *
from src.argument_manager import *
from src.push_mirror import *
from src.generate_mirror_workflow import *
from src.generate_folders_with_repo import *
from src.generate_mirror import *
from src.Github.Github import Github as Github
from src.SshKeyRepositoryParser.SshKeyRepositoryParserEpitech import SshKeyRepositoryParserEpitech
import os
from github import GithubException

DEFAULT_COMMIT: str = "CI/CD push"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def check_all(github: Github, sshParser: SshKeyRepositoryParserEpitech, mirror_name: str):
    try:
        organization = github.get_organization(sshParser.organizationName)
    except GithubException as err:
        print(f"{bcolors.FAIL}ERROR: Unable to find organization \"{sshParser.organizationName}\": "
              f"{str(err.args[1]['message'])}{bcolors.ENDC}")
        if err.args[1]['message'] == "Bad credentials":
            print(f"{bcolors.HEADER}You maybe need to change the token in data.json{bcolors.ENDC}")
        exit(84)
    try:
        repository = organization.get_repo(sshParser.repositoryName)
    except Exception as err:
        print(f"{bcolors.FAIL}ERROR: Unable to find repository \"{sshParser.repositoryName}\": "
              f"{str(err.args[1]['message'])}{bcolors.ENDC}")
        exit(84)
    user = github.get_user()
    try:
        user.get_repo(mirror_name)
        print(f"{bcolors.FAIL}ERROR: Unable to create repository: {mirror_name} already exist{bcolors.ENDC}")
        exit(84)
    except Exception as err:
        pass
    if os.path.isdir(sshParser.projectName):
        print(f"{bcolors.FAIL}ERROR: Unable to create directory: {sshParser.projectName} directory already exist{bcolors.ENDC}")
        exit(84)


def main():
    args = argumentManager()
    input_file = "data.json"
    if args.input_file is not None:
        input_file = args.input_file[0]
    json_file = json.load(open(input_file))
    if (json_file["token"] == "[your token]"):
        print(f"{bcolors.FAIL}You need to change the token in data.json{bcolors.ENDC}")
        exit(84)
    github = Github(json_file["token"])
    sshParser = SshKeyRepositoryParserEpitech(args.sshKey[0])
    try:
        sshParser.parse()
    except Exception as e:
        print(f"{bcolors.FAIL}{e}{bcolors.ENDC}")
        exit(84)
    mirror_name = f"{sshParser.projectName}-mirror"
    if args.mirror_name is not None:
        mirror_name = args.mirror_name[0]
    commit = DEFAULT_COMMIT
    if args.commit is not None:
        commit = args.commit[0]
    check_all(github, sshParser, mirror_name)
    generate_mirror(sshParser.organizationName, sshParser.repositoryName, github, mirror_name, args.project)
    generate_folders_with_repo(sshParser.sshKey, sshParser.projectName, github.get_user().get_login(), sshParser.repositoryName,
                               mirror_name)
    generate_mirror_workflow(sshParser.projectName, sshParser.repositoryName, mirror_name)
    add_collaborators(args.friend, mirror_name, github)
    push_mirror(mirror_name, sshParser.projectName, commit)


if __name__ == '__main__':
    main()
