[![Format](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/format.yml)

[![Install](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/install.yml)

[![Lint](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/lint.yml)

[![Test](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IndividualProject1_Shiyue_Zhou/actions/workflows/test.yml)

## Project Structure

* <h/> **Jupyter Notebook with:** </h>  
- Cells that perform descriptive statistics using Polars or Panda.  
- Tested by using nbval plugin for pytest  
* <h/> **Makefile with the following:** </h>  
- Run all tests (must test notebook and script and lib)  
- Formats code with Python black   
- Lints code with Ruff   
- Installs code via:  pip install -r requirements.txt  
<h/> </h>  
*   test_script.py to test script  
* test_lib.py to test library  
-- Pinned requirements.txt  
-- Gitlab Actions performs all four Makefile commands with badges for each one in the README.md  


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




