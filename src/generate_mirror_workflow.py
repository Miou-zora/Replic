#!/usr/bin/env python3
# @Miou-zora Project, Mirror-Generator, 2023

import subprocess


def generate_mirror_workflow(project_name: str,
                             repo_ssh: str,
                             mirror_name: str):
    f = open("verif_mirror.yml", "r")
    mirror_file_data = f.read()
    f.close()
    mirror_file_data = mirror_file_data.replace("MIRROR_URL_MIRROR_GENERATOR",
                                                repo_ssh)
    mirror_file_data = mirror_file_data.replace("EXECUTABLE_MIRROR_GENERATOR",
                                                project_name)
    actions = [(["mkdir", f"{project_name}/{mirror_name}/.github"],
                "Folder already exist: "
                + f"{project_name}/{mirror_name}/.github"),
               (["mkdir", f"{project_name}/{mirror_name}/.github/workflows"],
                "Folder already exist: "
                + f"{project_name}/{mirror_name}/.github/workflows")]
    for action in actions:
        if subprocess.run(action[0]).returncode == 1:
            raise Exception(action[1])
    mirror_file = open(f"{project_name}/{mirror_name}/\
        .github/workflows/verif_mirror.yml", "w")
    mirror_file.write(mirror_file_data)
    mirror_file.close()
