#!/usr/bin/env python3
##
## @Miou-zora PROJECT, 2023
## mirror-generator
## File description:
## main.py
##

from github import Github
from sys import argv
import json
from src.add_to_collaborators import *
from src.argument_manager import *
from src.push_mirror import *
from src.generate_mirror_workflow import *
from src.generate_folders_with_repo import *
from src.generate_mirror import *

def main():
    args = argumentManager()
    repo_info = args.sshKey[0].split(":")[1].split("/")
    json_file = json.load(open("data.json"))
    github_identifier: Github = Github(json_file["token"])
    orga_name = repo_info[0]
    repo_name = ".".join(repo_info[1].split(".")[:-1])
    generate_mirror(orga_name, repo_name, github_identifier)
    generate_folders_with_repo(args.sshKey[0], github_identifier.get_user().login, repo_name)
    generate_mirror_workflow(args.sshKey[0].split('-')[-2], args.sshKey[0], repo_name)
    add_collaborators(args.friend, f"{repo_name}-mirror", github_identifier)
    push_mirror(f"{repo_name}-mirror", args.sshKey[0].split('-')[-2])

if __name__ == '__main__':
    main()
