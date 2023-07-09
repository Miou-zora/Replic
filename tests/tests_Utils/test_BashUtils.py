#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

import unittest
from src.Utils.BashUtils import BashUtils
import os
import uuid


class TestBashUtils(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_mkdir(self):
        folder_name = str(uuid.uuid4()) + "_mkdir"
        if os.path.exists(folder_name):
            self.fail("Folder already exist: " + folder_name)
        BashUtils.mkdir(folder_name)
        if not os.path.exists(folder_name):
            self.fail("Folder not created: " + folder_name)
        os.rmdir(folder_name)

    def test_mkdir_already_exist(self):
        folder_name = str(uuid.uuid4()) + "_mkdir_already_exist"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        with self.assertRaises(Exception) as context:
            BashUtils.mkdir(folder_name)
        os.rmdir(folder_name)

    def test_mv(self):
        src_folder_name = str(uuid.uuid4()) + "_mv_src"
        dest_folder_name = str(uuid.uuid4()) + "_mv_dest"
        os.mkdir(src_folder_name)
        os.mkdir(dest_folder_name)
        BashUtils.mv(src_folder_name, dest_folder_name)
        if not os.path.exists(dest_folder_name + "/" + src_folder_name):
            self.fail("Folder not moved: " + src_folder_name)
        os.rmdir(dest_folder_name + "/" + src_folder_name)
        os.rmdir(dest_folder_name)

    def test_mv_src_not_exist(self):
        src_folder_name = str(uuid.uuid4()) + "_mv_src_not_exist"
        dest_folder_name = str(uuid.uuid4()) + "_mv_dest"
        os.mkdir(dest_folder_name)
        with self.assertRaises(Exception) as context:
            BashUtils.mv(src_folder_name, dest_folder_name)
        os.rmdir(dest_folder_name)
