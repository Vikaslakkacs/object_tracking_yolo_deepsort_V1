# Setting up basic stricuture of project like name, repository, name, etc
import setuptools

# Get the desription of the project by readme file
with open("README.md", 'r', encoding='utf-8') as readme:
    long_description = readme.read()

# Version is for package that is uploaded in pypi.org. Whenever we upload new changes then version has to be changed
__version__ = "0.0.0"
# Add Repo, author source and email of auther

REPO_NAME= "object_tracking_yolo_deepsort_V1"
AUTHOR_NAME= "vikaslakkacs"
SRC_REPO= "object_tracking_yolo_deepsort_V1"
AUTHOR_EMAIL= "vikaslakkacs@gmail.com"

# Setup tools configuration
setuptools.setup(
    name= REPO_NAME,
    version= __version__,
    author= AUTHOR_NAME,
    author_email= AUTHOR_EMAIL,
    description= "Object tracking using yolo and deepsort",
    long_description= long_description,
    long_description_content_type= "text/markdown",
    url= f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    packages= setuptools.find_packages(where="src"),
    project_urls={
        "Bug Reports": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
        "Source": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    },
    package_dir= {"":"src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)