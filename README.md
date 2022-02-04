# tutorials
Quick and dirty tutorials and templates 

# Annotations

`annotation.py` takes data from `./data/input/vfp_audios_16khz/` (just the first third of the speech task) dir and outputs a DF in `./data/outputs/annotations/` 

After verifying the paths and instructions in the first few lines, run:
```
pip3 install playsound PyObjC pandas 
python3 annotation.py
```


`annotation.ipynb` is a Colab approach. when you use `display.display(display.Audio(path))` in jupyter you can't include a input() in the next line. So this an alternative where all audio files are placed there. and one could splitscreen and manually label with a spreadsheet. 

