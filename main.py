#!/usr/bin/env python3
##
## @Miou-zora PROJECT, 2023
## mirror-generator
## File description:
## why do you look at this aweful code ...
##

from github import Github
from sys import argv
import json
from flag_friend.add_to_collaborators import *
from flag_friend.add_friend_in_list import *
from flag_friend.argument_manager import *
from push_mirror import *
from generate_mirror_workflow import *
from generate_folders_with_repo import *
from generate_mirror import *

def main():
    if len(argv) < 2:
        exit(84)

    args = argumentManager()
    github_usernames = []
    github_usernames = addfriendsinlist(args, github_usernames)
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
