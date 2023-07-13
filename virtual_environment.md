
# How to create a conda virtual environment

In a terminal, type: 
`conda create -n template python=3.9 pandas numpy scikit-learn seaborn matplotlib jupyterlab`

Change env_name to the name you want (I recommend short names because you will be typing it a lot)
COPY: `conda create --name new_name --clone template`
INFO: `conda info --envs`
SIZE: `du -h -s $(conda info --base)/envs/*`
REMOVE: `conda remove --name myenv --all`

### Changing Python interpreter in Spyder to your virtual environment


### Changing Python interpreter in PyCharm to your virtual environment
Preferences > Python Interpreter > Virtual Env > Existing + Make available to all projects
