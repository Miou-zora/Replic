#!/usr/bin/env python3
## @Miou-zora Project, Mirror-Generator, 2023

import github as gh
from .User import User

class Repository:
    def __init__(self, repo: gh.Repository.Repository) -> None:
        self.repo = repo
        
    def add_to_collaborators(self, user: User, permission: str):
        self.repo.add_to_collaborators(user, permission)
        
    def create_secret(self, name: str, value: str):
        self.repo.create_secret(name, value)
