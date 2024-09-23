[![Format](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/format.yml)

[![Install](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/install.yml)

[![Lint](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/lint.yml)

[![Test](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/test.yml)

## Continuous Integration using Gitlab Actions of Python Data Science Project

## Demo
https://youtu.be/UoD38zbSrUc

## Project Requirement

* <h/> **Jupyter Notebook with:** </h>  
- Cells that perform descriptive statistics using Polars or Panda.  
- Tested by using nbval plugin for pytest  
* <h/> **Makefile with the following:** </h>  
- Run all tests (must test notebook and script and lib)  
- Formats code with Python black   
- Lints code with Ruff   
- Installs code via:  pip install -r requirements.txt  
<h/> </h> 
* **test_script.py to test script**
* **test_lib.py to test library**  
* **Pinned requirements.txt**  
* **Gitlab Actions performs all four Makefile commands with badges for each one in the README.md**  



# Project Main Structure
This section explains the purpose of each file and directory in the project.
### **.devcontainer/**
Contains configuration files for setting up a development container environment, ensuring consistency in development setups.
### **.github/workflows/format.yml**
Defines a GitHub Actions workflow that automatically formats the codebase using tools like `black` or `prettier`.
### **.github/workflows/install.yml**
Specifies a GitHub Actions workflow that installs dependencies or sets up the project environment.
### **.github/workflows/lint.yml**
Configures a GitHub Actions workflow to run linting checks, ensuring the code follows the required style and quality standards.
### **.github/workflows/test.yml**
Sets up a GitHub Actions workflow to run tests, ensuring that the code passes all unit or integration tests.
### **mylib/lib.py**
Contains the core functionality or helper functions used across the project.
### **main.py**
The main entry point for the application, where the primary execution logic is implemented.
### **test_lib.py**
Holds unit tests for the functions or classes defined in `mylib/lib.py`, ensuring that they work as expected.
### **test_main.py**
Contains test cases for `main.py`, ensuring its logic and behavior are correct.
### **Makefile**
Defines automated commands for common tasks like building, testing, and cleaning the project.
### **requirements.txt**
Lists the Python dependencies required for the project to run, making it easy to install them with `pip`.
### **repeat.sh**
be used to automate repetitive tasks or to rerun certain operations continuously



## Template for Python projects with RUFF linter

* `Makefile`

* `Pytest`

* `pandas`

* `Ruff`:  

Run `make lint` which runs `ruff check`. 

* `Dockerfile`

* `GitHub copilot`

* `jupyter` and `ipython` 

* A base set of libraries for devops and web

* `githubactions`




