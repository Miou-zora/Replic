# Contribution guidelines

Thank you for considering contributing to my Replic project!

These guidelines are meant for new contributors, regardless of their level
of proficiency; following them allows the maintainers my Replic project to
more effectively evaluate your contribution, and provide prompt feedback to
you. Additionally, by following these guidelines you clearly communicate
that you respect the time and effort that the people developing Replic put into
managing the project.

#### Langage: English (or French for PR's review)

All interactions should be in English (or French for PR's review), to allow everyone to understand and participate.

### Description of the project

The goal of this project is to create a mirror repository of an another repository (currently it will only works with Epitech's repository).

## Table of Contents

- [Documentation](#documentation)
- [How to launch the project](#how-to-launch-the-project)
  - [Dependencies](#dependencies)
  - [Compilation](#compilation)
  - [Execution](#execution)
- [How to report a bug](#how-to-report-a-bug)
- [How to suggest a feature or enhancement](#how-to-suggest-a-feature-or-enhancement)
- [Where can I ask for help?](#where-can-i-ask-for-help)
- [Coding style](#coding-style)
- [Commit format](#commit-format)
- [Labels](#labels)
- [Branches](#branches)
- [Pull Requests](#pull-requests)
- [Milestone](#milestone)
- [Testing Policies](#testing-policies)
- [Author](#author)

## Documentation

There is no documentation for the moment. But you can maybe find some documentation in the code.

## How to launch the project

### Dependencies

To launch the project, you need to install the following dependencies:
- [Python 3.10.6](https://www.python.org/downloads/release/python-3106/)
- [Pip](https://pypi.org/project/pip/)

You will also need to install the following python packages:
- PyGithub 1.58.0
- coverage 7.2.7
- pytest 7.4.0
- pycodestyle 2.10.0

You can install them with the following command:
```
make install
```
/!\ Don't forget to install [Python 3.10.6](https://www.python.org/downloads/release/python-3106/) and [Pip](https://pypi.org/project/pip/) before. /!\

### Execution

To execute the project, there is help for it:
```
usage: main.py [-h] [--friend FRIEND] [--mirror-name MIRROR_NAME] [--commit COMMIT] sshKey

A beautiful mirror-generator.

positional arguments:
  sshKey                SSH key(s) to be added to the mirror repository.

options:
  -h, --help            show this help message and exit
  --friend FRIEND, -f FRIEND
                        Can add friend to mirror repository.
  --mirror-name MIRROR_NAME, -m MIRROR_NAME
                        Change the mirror repository name.
  --commit COMMIT, -o COMMIT
                        change the first commit push to the main repository
```
(You can also use `python3 main.py -h` for more informations)

## How to report a bug

If you find a bug, you can open an issue on the repository with bug report template.

## How to suggest a feature or enhancement

If you want to suggest a feature or enhancement, you can open an issue on the repository with feature template.

## Where can I ask for help?

You can ask for help to [me](https://github.com/Miou-zora) or on the issue/PR.

(When interacting with me, please be a human being)

## Coding style

We use pep8 coding style for this project. You can use `make coding_style` to check if your code is pep8 compliant and `make coding_style_details` to have more details about the pep8 errors.

## Commit format

In the project, we use [Angular Commit Convention](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)

## Labels

Each labels must be the type of the Issue.

## Branch

### Namming

Branch should have an automatic namming due to branch creation via issues. But if you create a branch from nothing you must use this template:

_branch-name_/_branch-description_

## Pull Requests (PR)

### Namming

If you create a PR, you must use this template:

[_pr name_] _pr description_

(In most of the case, you can reuse issue name)

### Process

#### Code review

For each PR we'll have a code review, the PR must be approved by [myself](https://github.com/Miou-zora).

#### PR Stability

Look at the [**Testing Policies**](#testing-policies)

#### Miscellaneous

Don't add to Replic github project except if the PR it.

Don't add to any Milestone of the project. If you doubt, ask it to [me](https://github.com/Miou-zora).

You can speak in French or English in the PR because I french and it's sometimes easier for me to talk in french above all for code review.

## Milestone

Milestone are used to organize the project. Each milestone must have a description and a due date. A milestone should be linked to an issue or a PR. A milestone should be linked to a set of functionnalities that makes the project works or a set of functionnalities that makes the project cohérent.

### Namming

If you create a milestone, you must use this template:

[_milestone-name_] _milestone description_

## Testing Policies

### Unit tests

Library: [unittest](https://docs.python.org/3/library/unittest.html)

### Unit tests (AI, GUI)

Please do unit tests if you can. We don't have a coverage goal for the moment.

### Functional tests

We don't force you to do functional tests other than indicated in issues but if you can do it, it's better.

### CI / CD

We have a really basic CI at the moment.

## Author

 - [Alexandre Franquet | Miouzora](https://github.com/Miou-zora)

