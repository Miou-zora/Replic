import unittest
from unittest.mock import patch, MagicMock, call
import sys
from argparse import Namespace

from src import argument_manager

class Testargument_manager(unittest.TestCase):
    
    all_parameters = {"friend": None, "mirror_name": None}

    @staticmethod
    def get_result_parsing(stdin_args: list[str]):
        with patch.object(sys, 'argv', stdin_args):
            args = argument_manager.argumentManager()
        return args

    def test_no_flag_no_ssh(self):
        with self.assertRaises(SystemExit) as se:
            args = argument_manager.argumentManager()
            
    def test_no_flag_with_ssh(self):
        param_result = self.get_result_parsing(["main.py", "ssh"])
        param_expected = {"sshKey": ["ssh"]}
        for value in self.all_parameters:
            if value not in param_expected:
                param_expected[value] = self.all_parameters[value]
        self.assertEqual(Namespace(**param_expected), param_result)
