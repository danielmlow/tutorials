
# Vscode 
- You can use colab, but eventually you'll want to switch to vscode for faster coding and debugging.
- Make sure you use shortcuts for everything and dont click things (its too slow). Key shortcut: highlight code in a .py script and running in a second panel interactive jupyter notebook window. After installing Jupyter extension in VS code, map "Jupyter: Run Selection/Line in Python Interactive Window" to command enter

Open your keybindings.json (Cmd+Shift+P → "Open Keyboard Shortcuts (JSON)") and ctrl+F (windows) or cmd+F (mac) "cmd+enter" and replace for "" for all commands except for `"command": "jupyter.execSelectionInteractive"` where you can add it again.

Then replace:
```
{
  "key": "cmd+enter",
  "command": "jupyter.execSelectionInteractive",
  "when": "editorTextFocus && isWorkspaceTrusted && jupyter.ownsSelection && !findInputFocussed && !isCompositeNotebook && !notebookEditorFocused && !replaceInputFocussed && editorLangId == 'python'"
}
```
for this:
```
{
  "key": "cmd+enter",
  "command": "jupyter.execSelectionInteractive",
  "when": "editorTextFocus && isWorkspaceTrusted && editorLangId == 'python'"
}
```


# Setting up virtual environment in miniconda
- https://github.com/danielmlow/tutorials/blob/main/run_python.md
- https://github.com/danielmlow/tutorials/blob/main/virtual_environment.md

# Statistics

- Basic intro: https://statsthinking21.github.io/statsthinking21-core-site/
  - In python: https://statsthinking21.github.io/statsthinking21-python/index.html
- Stats for experiments: https://experimentology.io/
  - It's in R, but you can try to work through the sections in Python.


# Machine Learning
# Intro
- https://sebastianraschka.com/blog/2020/intro-to-dl-ch01.html
- Basic pipeline: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

### My Machine learning pipeline checklist:
- https://docs.google.com/document/d/1xA8nz5CvB1iQaRbvFv0XRnPbkm7yYQ18lFcKmP-IFmY/edit?usp=sharing
- Python code (in progress): https://github.com/danielmlow/tutorials/blob/main/machine_learning/Machine_Learning_Checklist_Paper.ipynb

### A bit more in depth ML: https://sebastianraschka.com/blog/2021/ml-course.html
