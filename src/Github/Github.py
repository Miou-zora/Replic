#!/usr/bin/env python3
## @Miou-zora Project, Mirror-Generator, 2023

import github as gh
from .Organization import Organization

class Github:
    def __init__(self, token: str) -> None:
        self.token = token
        self.github: gh.Github = gh.Github(token)
        
    def get_user(self, user_name: str | None = None): # TODO: add return value type
        from .User import User
        if user_name == None:
            return User(self.github.get_user())
        return User(self.github.get_user(user_name))
    
    def get_organization(self, organization_name: str): # TODO: add return value type
        return Organization(self.github.get_organization(organization_name))
