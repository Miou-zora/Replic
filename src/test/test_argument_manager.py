#!/usr/bin/env python3
##
## @Miou-zora Project, Mirror-Generator, 2023
## test_argument_manager.py
## File description:
## Tests argument_manager file.
##

from unittest import TestCase
from unittest.mock import patch
import sys
from argparse import Namespace
import io
from contextlib import redirect_stdout, redirect_stderr
from src import argument_manager

class Testargument_manager(TestCase):
    all_parameters = {"friend": None, "mirror_name": None, "commit": None}

    @staticmethod
    def get_result_parsing(stdin_args: list[str]) -> Namespace:
        with patch.object(sys, 'argv', stdin_args):
            args = argument_manager.argumentManager()
        return args

    def compare_input_expected(self, stdin_args: list[str], expected: dict):
        param_result: Namespace = self.get_result_parsing(stdin_args)
        param_expected: dict = expected
        for value in self.all_parameters:
            if value not in param_expected:
                param_expected[value] = self.all_parameters[value]
        namespace_param_expected: Namespace = Namespace(**param_expected)
        self.assertEqual(namespace_param_expected, param_result)

    def test_help_flag(self):
        with self.assertRaises(SystemExit) as se:
            with io.StringIO() as buf, redirect_stdout(buf):
                self.get_result_parsing(["main.py", "-h"])
        sys.argv = []

    def test_no_flag_no_ssh(self):
        with self.assertRaises(SystemExit) as se:
            with io.StringIO() as buf, redirect_stderr(buf):
                self.get_result_parsing(["main.py"])
        sys.argv = []

    def test_no_flag_with_ssh(self):
        stdin_args: list[str] = ["main.py", "ssh"]
        expected: dict = {"sshKey": ["ssh"]}
        self.compare_input_expected(stdin_args, expected)

    def test_one_long_flag_mirror_name(self):
        stdin_args: list[str] = ["main.py", "ssh", "--mirror-name", "mirrorNameTest"]
        expected: dict = {"sshKey": ["ssh"], "mirror_name": ["mirrorNameTest"]}
        self.compare_input_expected(stdin_args, expected)

    def test_one_short_flag_mirror_name(self):
        stdin_args: list[str] = ["main.py", "ssh", "-m", "mirrorNameTest"]
        expected: dict = {"sshKey": ["ssh"], "mirror_name": ["mirrorNameTest"]}
        self.compare_input_expected(stdin_args, expected)

    def test_multiple_flag_mirror_name(self):
        stdin_args: list[str] = ["main.py", "ssh", "-m", "mirrorNameTest0", "-m", "mirrorNameTest1"]
        expected: dict = {"sshKey": ["ssh"], "mirror_name": ["mirrorNameTest1"]}
        self.compare_input_expected(stdin_args, expected)

    def test_multiple_same_flag_mirror_name(self):
        stdin_args: list[str] = ["main.py", "ssh", "-m", "mirrorNameTest", "-m", "mirrorNameTest"]
        expected: dict = {"sshKey": ["ssh"], "mirror_name": ["mirrorNameTest"]}
        self.compare_input_expected(stdin_args, expected)

    def test_one_long_flag_friend(self):
        stdin_args: list[str] = ["main.py", "ssh", "--friend", "friendTest"]
        expected: dict = {"sshKey": ["ssh"], "friend": ["friendTest"]}
        self.compare_input_expected(stdin_args, expected)

    def test_one_short_flag_friend(self):
        stdin_args: list[str] = ["main.py", "ssh", "-f", "friendTest"]
        expected: dict = {"sshKey": ["ssh"], "friend": ["friendTest"]}
        self.compare_input_expected(stdin_args, expected)

    def test_multiple_flag_friend(self):
        stdin_args: list[str] = ["main.py", "ssh", "-f", "friendTest0", "-f", "friendTest1"]
        expected: dict = {"sshKey": ["ssh"], "friend": ["friendTest0", "friendTest1"]}
        self.compare_input_expected(stdin_args, expected)

    def test_multiple_same_flag_friend(self):
        stdin_args: list[str] = ["main.py", "ssh", "-f", "friendTest", "-f", "friendTest"]
        expected: dict = {"sshKey": ["ssh"], "friend": ["friendTest"]}
        self.compare_input_expected(stdin_args, expected)

    def test_one_long_flag_commit(self):
        stdin_args: list[str] = ["main.py", "ssh", "--commit", "commitTest"]
        expected: dict = {"sshKey": ["ssh"], "commit": ["commitTest"]}
        self.compare_input_expected(stdin_args, expected)

    def test_one_short_flag_commit(self):
        stdin_args: list[str] = ["main.py", "ssh", "-o", "commitTest"]
        expected: dict = {"sshKey": ["ssh"], "commit": ["commitTest"]}
        self.compare_input_expected(stdin_args, expected)

    def test_multiple_flag_commit(self):
        stdin_args: list[str] = ["main.py", "ssh", "-o", "commitTest0", "-o", "commitTest1"]
        expected: dict = {"sshKey": ["ssh"], "commit": ["commitTest1"]}
        self.compare_input_expected(stdin_args, expected)

    def test_multiple_same_flag_commit(self):
        stdin_args: list[str] = ["main.py", "ssh", "-o", "commitTest", "-o", "commitTest"]
        expected: dict = {"sshKey": ["ssh"], "commit": ["commitTest"]}
        self.compare_input_expected(stdin_args, expected)

    def test_multiple_flag(self):
        stdin_args: list[str] = ["main.py", "ssh", "-m", "mirrorNameTest", "-f", "friendTest", "-o", "commitTest"]
        expected: dict = {"sshKey": ["ssh"], "mirror_name": ["mirrorNameTest"], "friend": ["friendTest"], "commit": ["commitTest"]}
        self.compare_input_expected(stdin_args, expected)
