
# Many resources
- https://docs.google.com/document/d/127Npk6Z2gV-p_ewwnRz7qDyvKKRI6vb6Yg3zKnOw16s/edit?usp=sharing

# Python
- Data Camp [link](https://www.datacamp.com/courses/intro-to-python-for-data-science?utm_source=google&utm_medium=paid_search&utm_campaignid=1565610606&utm_adgroupid=64773273292&utm_device=c&utm_keyword=datacamp%20python&utm_matchtype=e&utm_network=g&utm_adpostion=&utm_creative=733936254458&utm_targetid=kwd-1166778958503&utm_loc_interest_ms=&utm_loc_physical_ms=9001999&utm_content=brd~tech~python&utm_campaign=220808_1-sea~brd~branded_2-b2c_3-nam_4-rtw_5-na_6-na_7-le_8-pdsh-go_9-b-e_10-na_11-na-feb25&gad_source=1&gclid=CjwKCAiAzvC9BhADEiwAEhtlN1cFDQDFvKMEwjdPNk-8x9vvkEbBgb3SKq1Z3mXnzxZ9aQhr-bMnKBoCQUcQAvD_BwE)
- Youtube course https://www.youtube.com/watch?v=yKi9-BfbfzQ&t=6s&ab_channel=freeCodeCampEspa%C3%B1ol 
- https://pll.harvard.edu/course/cs50s-introduction-programming-python?delta=0
- Intro to Python (version 3): https://www.codecademy.com/learn/learn-python-3
- If that one at some point asks you to upgrade to Pro version, then this one should be free: Python version 2: https://www.codecademy.com/learn/learn-python
- https://aeturrell.github.io/coding-for-economists/code-preliminaries.html
- Pandas: 
- https://aeturrell.github.io/coding-for-economists/data-analysis-quickstart.html
- Interactive Colab book on Pandas, numpy, machine learning: https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.01-Introducing-Pandas-Objects.ipynb#scrollTo=a9CSUN-4sRi-

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

# Causal inference
- General intro: https://medium.com/data-science-at-microsoft/causal-inference-part-1-of-3-understanding-the-fundamentals-816f4723e54a
- https://press.princeton.edu/books/hardcover/9780691199429/data-analysis-for-social-science
- Gelman, A., Hill, J., & Vehtari, A. (2021). Regression and Other Stories. Cambridge University Press.
- Free: Online and implementation in R https://mixtape.scunning.com/
- Free: Book, videos, and slides: https://www.bradyneal.com/causal-inference-course
- Free: More advanced (free, online, videos, book) https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2023/home
  - Book: https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/



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


# Using LLMs to do qualitative coding
- Tutorial: https://github.com/danielmlow/llm_course/blob/main/openrouter_api.ipynb

- Workshop video (2hs): https://mindandlife.zoom.us/rec/share/MvBsiFDPoKERnJktnsLYn2UOjGynrFPUlo-tjamaO-HEOj7IeF-I7Gyk6W4lvquL.GsgMEEcFb7Lxf2j8?startTime=1761753753000
  - Passcode: 6.#ZxEDK

- Tutorials from workshop: https://github.com/danielmlow/llm_course

- Codebook for 49 suicide risk factors: https://github.com/danielmlow/construct-tracker/blob/main/src/construct_tracker/data/lexicons/suicide_risk_lexicon_v1-0/suicide_risk_lexicon_codebook_prototypical_examples.txt
