#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

import abc


class ASshKeyRepositoryParser(abc.ABC):
    def __init__(self, sshKey: str = None):
        self.sshKey = sshKey
        self.organizationName = None
        self.repositoryName = None
        self.projectName = None

    @abc.abstractmethod
    def parse(self):
        pass
