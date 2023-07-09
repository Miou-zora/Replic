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
