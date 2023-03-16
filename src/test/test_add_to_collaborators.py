import unittest
from unittest.mock import patch, MagicMock, call

from github import GithubException
from src import add_to_collaborators

class Testadd_collaborators(unittest.TestCase):

    @patch('src.add_to_collaborators.Github')
    def test_no_user(self, github):
        
        repo_mock = MagicMock()
        
        user_mock = MagicMock()
        user_mock.get_repo.return_value = repo_mock
        
        def side_effect(name="thereIsNoName"):
            possibleName = ["user1", "user2"]
            if name in possibleName:
                return user_mock
            elif name == "thereIsNoName":
                return user_mock
            else:
                raise GithubException(84, "Unvalid Username", None)
        
        github.get_user.side_effect = side_effect
        
        users = []
        repo_name = "repo_name"
        
        add_to_collaborators.add_collaborators(users, repo_name, github)
        
        github.assert_has_calls([call.get_user()])
        self.assertEqual(repo_mock.call_count, 0)
        
    @patch('src.add_to_collaborators.Github')
    def test_two_user(self, github):
        
        repo_mock = MagicMock()
        repo_mock.add_to_collaborators.return_value = None
        
        user_mock = MagicMock()
        user_mock.get_repo.return_value = repo_mock
        
        def side_effect(name="thereIsNoName"):
            possibleName = ["user1", "user2"]
            if name in possibleName:
                return user_mock
            elif name == "thereIsNoName":
                return user_mock
            else:
                raise GithubException(84, "Unvalid Username", None)
        
        github.get_user.side_effect = side_effect
        
        users = ["user1", "user2"]
        repo_name = "repo_name"
        
        add_to_collaborators.add_collaborators(users, repo_name, github)
    
        github.assert_has_calls([call.get_user(), call.get_user(users[0]), call.get_user(users[1])])
        repo_mock.add_to_collaborators.assert_has_calls(
            [call.get_user(github.get_user(users[0]), "push"),
             call.get_user(github.get_user(users[1]), "push")])
        
    @patch('src.add_to_collaborators.Github')
    def test_bad_user(self, github):

        repo_mock = MagicMock()
        
        user_mock = MagicMock()
        user_mock.get_repo.return_value = repo_mock
        
        def side_effect(name="thereIsNoName"):
            possibleName = ["user1", "user2"]
            if name in possibleName:
                return user_mock
            elif name == "thereIsNoName":
                return user_mock
            else:
                raise GithubException(84, "Unvalid Username", None)
        
        github.get_user.side_effect = side_effect
        
        users = ["notAUser"]
        repo_name = "repo_name"
        
        with self.assertRaises(Exception) as err:
            add_to_collaborators.add_collaborators(users, repo_name, github)
        self.assertEqual(f"User {users[0]} does not exist", str(err.exception))

        github.assert_has_calls([call.get_user(), call.get_user(users[0])])
        self.assertEqual(repo_mock.call_count, 0)

    @patch('src.add_to_collaborators.Github')
    def test_none_user(self, github):
        
        repo_mock = MagicMock()
        
        user_mock = MagicMock()
        user_mock.get_repo.return_value = repo_mock
        
        def side_effect(name="thereIsNoName"):
            possibleName = ["user1", "user2"]
            if name in possibleName:
                return user_mock
            elif name == "thereIsNoName":
                return user_mock
            else:
                raise GithubException(84, "Unvalid Username", None)
        
        github.get_user.side_effect = side_effect
        
        users = None
        repo_name = "repo_name"
        
        add_to_collaborators.add_collaborators(users, repo_name, github)
        
        github.assert_has_calls([call.get_user()])
        self.assertEqual(repo_mock.call_count, 0)

if __name__ == "__main__":
    unittest.main()
