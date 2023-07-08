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
from src.SshKeyRepositoryParser.SshKeyRepositoryParserEpitech import \
    SshKeyRepositoryParserEpitech

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


def main():
    args = argumentManager()
    json_file = json.load(open("data.json"))
    if (json_file["token"] == "[your token]"):
        print(f"{bcolors.FAIL}You need to change the \
                token in data.json{bcolors.ENDC}")
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
    commit = (args.commit[0] if (args.commit is not None) else DEFAULT_COMMIT)
    generate_mirror(sshParser.organizationName,
                    sshParser.repositoryName, github, mirror_name)
    generate_folders_with_repo(sshParser.sshKey, sshParser.projectName,
                               github.get_user().get_login(),
                               sshParser.repositoryName,
                               mirror_name)
    generate_mirror_workflow(sshParser.projectName,
                             sshParser.repositoryName, mirror_name)
    add_collaborators(args.friend, mirror_name, github)
    push_mirror(mirror_name, sshParser.projectName, commit)


if __name__ == '__main__':
    main()
