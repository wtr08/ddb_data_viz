# Funda AI Project

IMPORTANT to contributors:
1. Comment to contributors. Add a folder "data" in the root folder, after the project has been cloned. Gitignore will neglect the "data" folder. Link to datasets: https://drive.google.com/drive/folders/1T9CvMdY6XCnMUqCuxfAk_ixe9joLqAYs?usp=sharing
2. the source code should reside in modules consisting of classes and functions (no top level code) in a folder at the top level (see the forecasting folder above . This folder should contain an empty __init__.py file so that python recognizes it as a package. Moreover, the setup.py file should point to this folder in the packages() line (see template). With this setup, you can create a conda environment with

```
conda create --name myenvironment python==3.8.5
```

and then do (from within your package folder):

```
conda activate myenvironment
pip install -e .
```

This then allows you to import modules from the package folder inside your run/run.py script, which
should be the script implementing the pipeline steps (i.e., the script called from command line).

