#!/usr/bin/env python3
##
## @Miou-zora Project, Mirror-Generator, 2023
##

from .ASshKeyRepositoryParser import ASshKeyRepositoryParser

class SshKeyRepositoryParserEpitech(ASshKeyRepositoryParser):
    def __init__(self, sshKey: str = None):
        super().__init__(sshKey)
        
    def parse(self):
        if self.sshKey == None:
            raise Exception("SshKeyRepositoryParserEpitech: No ssh key given.")
        try:
            self.organizationName = self.sshKey.split(":")[1].split("/")[0]
        except:
            raise Exception("SshKeyRepositoryParserEpitech: Invalid ssh key: organization name not found.")
        try:
            self.repositoryName = ".".join(self.sshKey.split(":")[1].split("/")[1].split(".")[:-1])
        except:
            raise Exception("SshKeyRepositoryParserEpitech: Invalid ssh key: repository name not found.")
        try:
            self.projectName = self.repositoryName.split("-")[-2]
        except:
            raise Exception("SshKeyRepositoryParserEpitech: Invalid ssh key: project name not found.")
