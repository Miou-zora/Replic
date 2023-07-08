#!/usr/bin/env python3
## @Miou-zora Project, Mirror-Generator, 2023

import Github as gh

class Github:
    def __init__(self, token: str) -> None:
        self.token = token
        self.github: gh.Github = gh.Github(token)
        
    def get_user(self, user_name: str): # TODO: add return value type
        return self.github.get_user(user_name)
    
    def get_organization(self, organization_name: str): # TODO: add return value type
        pass
