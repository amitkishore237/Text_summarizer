import os
from pathlib import Path
import logging #for logging

#create logging stream
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="text_summarizer"

#list of files and foolders that will be created

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/constant.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/test.ipynb"
]


#create directories and files
for filepath in list_of_files:
    #create directories
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    #foldercreation
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory:{filedir} for the filename{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"{filename} already exists")

