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

from src import argument_manager

class Testargument_manager(TestCase):
    
    all_parameters = {"friend": None, "mirror_name": None}

    @staticmethod
    def get_result_parsing(stdin_args: list[str]) -> Namespace:
        with patch.object(sys, 'argv', stdin_args):
            args = argument_manager.argumentManager()
        return args

    def test_no_flag_no_ssh(self):
        with self.assertRaises(SystemExit) as se:
            self.get_result_parsing(["main.py"])
            
    def test_no_flag_with_ssh(self):
        param_result: Namespace = self.get_result_parsing(["main.py", "ssh"])
        param_expected: dict = {"sshKey": ["ssh"]}
        for value in self.all_parameters:
            if value not in param_expected:
                param_expected[value] = self.all_parameters[value]
        self.assertEqual(Namespace(**param_expected), param_result)
    
    def test_flag_mirror_name(self):
        param_result: Namespace = self.get_result_parsing(["main.py", "ssh", "--mirror-name", "mirrorNameTest"])
        param_expected: dict = {"sshKey": ["ssh"], "mirror_name": ["mirrorNameTest"]}
        for value in self.all_parameters:
            if value not in param_expected:
                param_expected[value] = self.all_parameters[value]
        self.assertEqual(Namespace(**param_expected), param_result)
