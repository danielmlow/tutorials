TL;DR: 

- You can start playing around with python using Google Colab [https://colab.research.google.com/](https://colab.research.google.com/) and choose `New notebook`. You can install packages Colab doesn't have using `!pip install package_name` 
- Eventually you'll want to download an interactive development environment (IDE) like Spyder, VScode, or pycharm and use package manager, either anaconda or miniconda, don't install both as it will mess up operability.
- make sure you can import theses packages:

```
import statsmodels.api as sm
import pydataset
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt 
import xgboost
```


# Virtual environments (anaconda or miniconda)
---


- Different code might need different package versions. You might need to upgrade or downgrade package A so package B works (since perhaps it was created using the an older version of package A). Once everything is working, you save all versions in a requirements.txt file so others can recreate virtual environment and run code without issues. 
- Each project or even some individual analysis within a project should have its own. 
- Someone may not be able to reproduce because differences OS could cause issues with installations. 
- This can all be done through miniconda. 
- To avoid doing all this (which is easy to do once you learn how), you can just download a distribution of thousands of packages that are guaranteed to work together called Anaconda Distribution. You can also manage install new packages and create virtual environments using the graphical interface called Anaconda Navigator, which may be better for beginners.  

### Running Python for beginners (anaconda)

For first-time users, Anaconda provides many packages pre-installed and a navigator interface for installing an IDEA and new packages that's easy to use.

1. Install Anaconda for your operating system: https://docs.anaconda.com/free/anaconda/install/ 
2. Anaconda Navigator will prompt you to sign in. You don't need to sign in to use and I had trouble creating an account. But if you want, create an account and sign in.
3. Install and then launch Spyder. 
4. By default, packages installed using your terminal will be installed to your base (root) environment. You can install packages using Anaconda Navigator https://docs.anaconda.com/free/navigator/tutorials/manage-packages/#installing-a-package

### Minimal virtual environments (miniconda)

1. Install miniconda (pkg is easiest): https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links
2. In a terminal or console, run the following replacing setting your environment name after the `-n` argument to something meaningful for this project (I recommend short names because you will be typing it a lot). Here I'll choose `ml`: 

`conda create -y -n ml python=3.10 pandas numpy scikit-learn seaborn matplotlib xgboost pydataset`

To use: 

`conda activate ml` # activate each time you start a new terminal so that you're operating inside the virtual environment

`conda install -y jupyterlab` # install another package with conda. 

**Use pip installer if package not available on conda**

Install additional packages:
`pip install pydataset spyder-kernels==2.4.*` # install other packages. spyder-kernels is needed to use the virtual environment in Spyder IDE. 

`pip install ` 

If for some reason you don't have pip (it comes with anaconda and miniconda), in the terminal, install pip: `python -m ensurepip --upgrade`. More info`https://pip.pypa.io/en/stable/installation/`

Other commands:

- INFO (see which envs you have): `conda info --envs`
- SIZE: `du -h -s $(conda info --base)/envs/*`
- REMOVE: `conda remove --name env_name --all`
- Clone another env: `conda create --name project2_name --clone project1_name`
- Save package versions at the end of your project: 
 - `pip freeze > requirements.txt`
 - 

**Change Python interpreter to your virtual environment**

**Spyder.** Then change Python interpreter in Spyder to your virtual environment. Go to Preferences > Python Interpreter > Use the following Python interpreter: `/Users/danielmlow/miniconda3/envs/psy2085/bin/python`

**PyCharm.** Preferences > Python Interpreter > Virtual Env > Existing + Make available to all projects


**conda not found error**

- In the terminal:
  `open ~/.bash_profile` or `open ~/.bashrc`
- Add the following line at the end of the file/s:
  `export PATH=~/miniconda3/bin:$PATH`
- Save and close the file. Then, in the terminal, source the file to apply the changes: `source ~/.bashrc`
- link conda to miniconda: `source ~/miniconda3/bin/activate`
- tell your computer to launch conda from your shell `conda init bash` (assuming you're using bash, if not check which one here: `ps -p $$`)

