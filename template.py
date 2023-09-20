"""
this file is responsible for creating the project file structure/project template
when run this file automatically create file structure otherwise you can do ot manually also
"""
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "TextSummerizer"

list_of_files = [
    ".github/workflows/.gitkeep",  #.github is helps for CICD pipelines
    f"src{project_name}/__init__.py", #for make this local package
    f"src{project_name}/components/__init__.py",
    f"src{project_name}/utils/__init__.py",
    f"src{project_name}/utils/common.py",
    f"src{project_name}/logging/__init__.py",
    f"src{project_name}/config/__init__.py",
    f"src{project_name}/config/configuration.py",
    f"src{project_name}/pipeline/__init__.py",
    f"src{project_name}/entity/__init__.py",
    f"src{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requrements.txt",
    "setup.py",
    "research/trails.ipynb"
]


for filepath in list_of_files:
    #to handle path issues
    filepath = Path(filepath)
    #split filepath and the file
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory {filedir} for the file {filename}")

    
    #filesize != 0 means, there are some code inside the file, then keep it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")


    