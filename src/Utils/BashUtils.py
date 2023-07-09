#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

import subprocess


class BashUtils:
    @staticmethod
    def mkdir(path: str):
        if subprocess.run(["mkdir", path]).returncode == 1:
            raise Exception("Folder already exist: " + path)

    @staticmethod
    def mv(src: str, dest: str):
        if subprocess.run(["mv", src, dest]).returncode == 1:
            raise Exception("Can't move folder: " + src)

    class Git:
        @staticmethod
        def add(where: str = ".", what: list[str] = ["."]):
            if subprocess.run(["git", "-C", where, "add", *what]).returncode == 1:
                raise Exception("No add can be done")

        @staticmethod
        def push(where: str = "."):
            if subprocess.run(["git", "-C", where, "push"]).returncode == 1:
                raise Exception("No push can be done")

        @staticmethod
        def commit(message: str, where: str = "."):
            if subprocess.run(["git", "-C", where, "commit", "-m", message]).returncode == 1:
                raise Exception("No commit can be done")

        @staticmethod
        def clone(ssh_key: str):
            if subprocess.run(["git", "clone", ssh_key]).returncode == 1:
                raise Exception("Can't clone repository: " + ssh_key)
