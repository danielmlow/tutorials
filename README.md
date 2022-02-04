# Tutorials
Quick and dirty tutorials and templates 

# Annotations

`annotation.py` takes data from `./data/input/vfp_audios_16khz/` (just the first third of the speech task) dir and outputs a DF in `./data/outputs/annotations/` 

Obtain `vfp_audios_16khz/` cannot be shared. Ask for it. 

After verifying the paths and instructions in the first few lines, run:
```
pip3 install playsound PyObjC pandas 
python3 annotation.py
```

### Colab option
`annotation.ipynb` is a Colab approach. when you use `display.display(display.Audio(path))` in jupyter you can't include a input() in the next line. So this is an alternative approach where all audio files are listed  and one can splitscreen and manually label with a spreadsheet. 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/annotation.ipynb)


