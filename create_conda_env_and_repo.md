# Prerequisits


Install GitHub CLI and log in to your GitHub account (or set a GH_TOKEN environment variable)

```
brew install gh
gh auth login
```

Make the Script Executable
```
chmod +x create_conda_env_and_repo.sh
```

# Script
Put in `create_conda_env_and_repo.sh`

```
#!/bin/bash

# Enable debugging to print each command
set -x

# Check if the required arguments are provided
if [ $# -lt 1 ]; then
  echo "Usage: $0 <env_name> [repo_name]"
  exit 1
fi

# Assign the first argument to ENV_NAME
ENV_NAME=$1

# If only one argument is provided, set REPO_NAME to the same as ENV_NAME
if [ $# -eq 1 ]; then
  REPO_NAME=$ENV_NAME
else
  REPO_NAME=$2
fi

# Step 1: Create a private GitHub repository using gh CLI
echo "Creating private GitHub repository: $REPO_NAME"
gh repo create "$REPO_NAME" --private

if [ $? -eq 0 ]; then
  echo "Repository '$REPO_NAME' created successfully."
else
  echo "Failed to create the repository."
  exit 1
fi

# Step 2: Create a directory for the repo in /Users/danielmlow/code
echo "Creating directory '/Users/danielmlow/code/$REPO_NAME'"
mkdir -p "/Users/danielmlow/code/$REPO_NAME"

# Step 3: Create a README.md file and data dirs in the directory
echo "# $REPO_NAME" > "/Users/danielmlow/code/$REPO_NAME/README.md"
echo "Virtual Environment: $ENV_NAME" > "/Users/danielmlow/code/$REPO_NAME/README.md"
mkdir -p data/input data/output data/manuscript

# Step 4: Initialize a local Git repository and link it to GitHub
echo "Initializing Git repository locally"
cd "/Users/danielmlow/code/$REPO_NAME" || exit
git init
git branch -m main

echo "Linking local repository to remote repository"
git remote add origin "https://github.com/$(gh auth status --show-token | grep 'Logged in to' | awk '{print $NF}')/$REPO_NAME.git"

# Set the correct remote URL for the GitHub repository
git remote set-url origin https://github.com/danielmlow/$REPO_NAME.git

# Step 5: Commit and push the README.md file
git add .
git commit -m "Initial commit"
git push -u origin main

# # Step 6: Create the Conda virtual environment
# echo "Creating conda environment: $ENV_NAME with Python 3.11"
# conda create -y -n "$ENV_NAME" python=3.11 seaborn ipywidgets

# if [ $? -eq 0 ]; then
#   echo "Environment '$ENV_NAME' created successfully."
# else
#   echo "Failed to create the environment."
#   exit 1
# fi

# echo "Done! The Conda environment '$ENV_NAME' is ready, the GitHub repository '$REPO_NAME' has been created, and the directory is set up at '/Users/danielmlow/code/$REPO_NAME'."
```


# Run the script
The second argument is optional. If not provided, both env and repo will be called the same. 
```
bash create_venv_repo.sh my_env_name my_repo_name
```
