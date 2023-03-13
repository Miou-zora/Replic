import unittest
from unittest.mock import patch, MagicMock

from github import GithubException
from src import add_to_collaborators

class Testadd_collaborators(unittest.TestCase):
    
    @patch('src.add_to_collaborators.Github')
    def test_no_user(self, mock_github):
        
        mock_repo = MagicMock()
        
        mock_user = MagicMock()
        mock_user.get_repo.return_value = mock_repo
        
        def side_effect(name="thereIsNoName"):
            if name == "user1":
                return mock_user
            elif name == "thereIsNoName":
                return mock_user
            else:
                raise GithubException(84, "Unvalid Username", None)
        
        mock_github.get_user.side_effect = side_effect
        
        add_to_collaborators.add_collaborators([], "repo_name", mock_github)
        
    @patch('src.add_to_collaborators.Github')
    def test_one_user(self, mock_github):
        mock_repo = MagicMock()
        
        mock_user = MagicMock()
        mock_user.get_repo.return_value = mock_repo
        
        def side_effect(name="thereIsNoName"):
            possibleName = ["user1", "user2"]
            if name in possibleName:
                return mock_user
            elif name == "thereIsNoName":
                return mock_user
            else:
                raise GithubException(84, "Unvalid Username", None)
        
        mock_github.get_user.side_effect = side_effect
        
        add_to_collaborators.add_collaborators(["user1", "user2"], "repo_name", mock_github)
        
    @patch('src.add_to_collaborators.Github')
    def test_bad_user(self, mock_github):
        mock_repo = MagicMock()
        
        mock_user = MagicMock()
        mock_user.get_repo.return_value = mock_repo
        
        def side_effect(name="thereIsNoName"):
            possibleName = ["user1", "user2"]
            if name in possibleName:
                return mock_user
            elif name == "thereIsNoName":
                return mock_user
            else:
                raise GithubException(84, "Unvalid Username", None)
        
        mock_github.get_user.side_effect = side_effect
        
        with self.assertRaises(Exception):
            add_to_collaborators.add_collaborators(["notAUser"], "repo_name", mock_github)

if __name__ == "__main__":
    unittest.main()
