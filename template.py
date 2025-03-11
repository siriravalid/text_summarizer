import os # libraries
from pathlib import Path
import logging #since we are logging all info

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # mention log level, give template how you want it

project_name = "textSummarizer"

#variable
list_of_files = [
    ".github/workflows/.gitkeep", #for cicd deployment yaml file, if we commit if github is empty it will not commit thats why we need gitkeep later we can delete
    f"src/{project_name}/__init__.py", #constructor file.. if we want to import as local file, constrcutor file is needed
    f"src/{project_name}/conponents/__init__.py",# need constructor file for all folders
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",#training, predciiton things
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")