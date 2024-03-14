from pathlib import Path  
from setuptools import find_packages, setup  


# Package meta-data
NAME = 'hpp-regression-model'
DESCRIPTION = 'New Approach to package model using regression algorithm.'
URL = "https://github.com/kempsly/ml-model-deploying-new-approach"
EMAIL = "kempslysilencieux3@gmail.com"
AUTHOR = "Kempsly"
REQUIRES_PYTHON = ">=3.8.18"

long_description = DESCRIPTION 

# Load the package's VERSION file as a dictionary.
about = {}
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR / 'requirements'
PACKAGE_DIR = ROOT_DIR / 'regression_model'

with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version
    

# required packages for this module to be executed?
def list_reqs(fname='requirements.txt'):
    with open(REQUIREMENTS_DIR / fname) as fd:
        return fd.read().splitlines()
    


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    package_data ={"regression_model": ["VERSION"]},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    licence="BSD-3",
    classifiers=[
        # Trove classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
],

    
)



