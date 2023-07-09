#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

import unittest
from src.Utils.BashUtils import BashUtils
import os


class TestBashUtils(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_mkdir(self):
        folder_name = "test_folder"
        if os.path.exists(folder_name):
            self.fail("Folder already exist: " + folder_name)
        BashUtils.mkdir(folder_name)
        if not os.path.exists(folder_name):
            self.fail("Folder not created: " + folder_name)
        os.rmdir(folder_name)
