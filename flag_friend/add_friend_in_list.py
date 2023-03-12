#!/usr/bin/env python3
##
## @VyOkPROJECT, 2023
## mirror-generator
## File description:
## why do you look at this aweful code ...
##

def addfriendsinlist(args, github_usernames):
    if args.friend:
        for friend in args.friend:
            if friend != args.friend[-1]:
                github_usernames.append(friend)
    return github_usernames
