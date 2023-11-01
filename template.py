### Creating skeletons for project
import os
from pathlib import Path ## Helps in creating paths (manages forward and backward slashes according to os)
import logging ## logging


## Define logging configuraion
logging.basicConfig(level= logging.INFO, format= '[%(asctime)s]: [%(message)s]')
project_name= "object_tracking_yolo_deepsort_V1"


##Create list of necessary files for project
list_of_project_files=[
    ".github/workflows/.getkeep", ## for CI/CD pipelines
    ## Src (script folders)
    f"src/{project_name}/_init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    "configs/config.yaml", ## Project configuration
    "dvc.yaml", # Data version control
    "params.yaml", ## project/model parameters
    "init_setup.sh", ## bash script helps in creating environtment and install requried packages
    "setup.py",
    "setup.cfg",
    "requirements.txt", # project requirements
    "requirements_dev.txt", # Project development requirements
    "pyproject.toml", # For python package creation
    "tox.ini", # For project testing locally
    "research/stage_01.ipynb", # Jupyter notebook for research
    "research/stage_02.ipynb",
    "research/stage_03.ipynb",
    "tests/__init__.py", ## for testing the project
    "tests/unit/__init__.py",
    "tests/integration/__init__.py"
    
]

##    Create Project related files. Before creation check for the parent folder whether it is created or not, if not then parent folder is created


for filepath in list_of_project_files:
    ## Get os related file path
    filepath= Path(filepath)

    ## Extracting folder name from the path
    file_dir, filename= os.path.split(filepath)
    print(filepath, file_dir)

    ## When there is no file directory then it is a file else we have to create directory

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"File directory: {file_dir}: has been created for file: {filename}")
    
    ##Creating files inside directory
    if not(os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            logging.info(f"File: {filename} has been created")
            pass
    else:
        logging.info(f"file {filename} already exists")
