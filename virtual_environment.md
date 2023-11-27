
# How to create a conda virtual environment

Install 
- miniconda (which only comes with the installer, usually pkg version is easiest): https://docs.conda.io/en/latest/miniconda.html
- or anaconda (which comes with many packages pre-installed): https://conda.io/projects/conda/en/latest/user-guide/install/index.html

In a terminal, run the following replacing env_name to something meaningful for this project (I recommend short names because you will be typing it a lot): 

`conda create -y -n env_name python=3.10 pandas numpy scikit-learn seaborn matplotlib jupyterlab`

To use: 

`conda activate env_name` # activate each time you start a new terminal

`conda install -y plotly` # install another package 

`pip install another_package` # install another package using pip if not available on conda

You can also make a template and copy it as you create other projects

`conda create -n template python=3.9 pandas numpy scikit-learn seaborn matplotlib jupyterlab`

`conda create --name project1_name --clone template`

`conda create --name project2_name --clone template`


Other commands:
- INFO: `conda info --envs`
- SIZE: `du -h -s $(conda info --base)/envs/*`
- REMOVE: `conda remove --name env_name --all`

### Changing Python interpreter in Spyder to your virtual environment
https://docs.spyder-ide.org/current/faq.html#using-existing-environment

### Changing Python interpreter in PyCharm to your virtual environment
Preferences > Python Interpreter > Virtual Env > Existing + Make available to all projects
