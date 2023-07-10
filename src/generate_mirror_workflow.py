#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

from .Utils.BashUtils import BashUtils


def generate_mirror_workflow(project_name: str, repo_ssh: str, mirror_name: str):
    f = open("verif_mirror.yml", "r")
    mirror_file_data = f.read()
    f.close()
    mirror_file_data = mirror_file_data.replace("MIRROR_URL_MIRROR_GENERATOR", repo_ssh)
    mirror_file_data = mirror_file_data.replace("EXECUTABLE_MIRROR_GENERATOR", project_name)
    mirror_folder = f"{project_name}/{mirror_name}"
    BashUtils.mkdir(f"{mirror_folder}/.github")
    BashUtils.mkdir(f"{mirror_folder}/.github/workflows")
    mirror_file = open(f"{mirror_folder}/.github/workflows/verif_mirror.yml", "w")
    mirror_file.write(mirror_file_data)
    mirror_file.close()
