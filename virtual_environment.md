
# How to create a conda virtual environment

In a terminal, type: 

`conda create -n template python=3.9 pandas numpy scikit-learn seaborn matplotlib jupyterlab`

Change `env_name` to the name you want (I recommend short names because you will be typing it a lot)
- COPY: `conda create --name env_name --clone template`

`conda activate env_name` # activate each time you start a new terminal
`pip install plotly` # install another package 

Other commands:
- INFO: `conda info --envs`
- SIZE: `du -h -s $(conda info --base)/envs/*`
- REMOVE: `conda remove --name env_name --all`

### Changing Python interpreter in Spyder to your virtual environment

TODO

### Changing Python interpreter in PyCharm to your virtual environment
Preferences > Python Interpreter > Virtual Env > Existing + Make available to all projects
