#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

import github as gh


class User:
    def __init__(self, user: gh.NamedUser.NamedUser | gh.NamedUser.NamedUser = None) -> None:
        self.user = user

    # TODO: add return value type
    def get_repo(self, repo_name: str):
        from .Repository import Repository
        return Repository(self.user.get_repo(repo_name))

    def create_repo(self,
                    name: str,
                    description: str = gh.GithubObject.NotSet,
                    homepage: str = gh.GithubObject.NotSet,
                    private: bool = gh.GithubObject.NotSet,
                    has_issues: bool = gh.GithubObject.NotSet,
                    has_wiki: bool = gh.GithubObject.NotSet,
                    has_downloads: bool = gh.GithubObject.NotSet,
                    has_projects: bool = gh.GithubObject.NotSet,
                    auto_init: bool = gh.GithubObject.NotSet,
                    license_template: str = gh.GithubObject.NotSet,
                    gitignore_template: str = gh.GithubObject.NotSet,
                    allow_squash_merge: bool = gh.GithubObject.NotSet,
                    allow_merge_commit: bool = gh.GithubObject.NotSet,
                    allow_rebase_merge: bool = gh.GithubObject.NotSet,
                    delete_branch_on_merge: bool = gh.GithubObject.NotSet):
        if self.user is None:
            raise Exception("User: Unable to create repo because user is None")
        if name is None:
            raise Exception("User: Unable to create repo because repository name is None")
        self.user.create_repo(
            name,
            description=description,
            homepage=homepage,
            private=private,
            has_issues=has_issues,
            has_wiki=has_wiki,
            has_downloads=has_downloads,
            has_projects=has_projects,
            auto_init=auto_init,
            license_template=license_template,
            gitignore_template=gitignore_template,
            allow_squash_merge=allow_squash_merge,
            allow_merge_commit=allow_merge_commit,
            allow_rebase_merge=allow_rebase_merge,
            delete_branch_on_merge=delete_branch_on_merge
        )

    def get_login(self):
        return self.user.login
