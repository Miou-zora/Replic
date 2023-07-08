#!/usr/bin/env python3
## @Miou-zora Project, Mirror-Generator, 2023

import github as gh

class Organization:
    def __init__(self, orga: gh.Organization.Organization) -> None:
        self.orga = orga
        
    def get_repo(self, repo_name: str):
        from .Repository import Repository
        return Repository(self.orga.get_repo(repo_name))
