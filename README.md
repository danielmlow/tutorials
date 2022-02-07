




# Tutorials
Quick and dirty tutorials and templates 

# Automatic speech recognition (ASR)
`asr.ipynb` uses SpeechBrain models 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/asr.ipynb)



# Speech Activity Detection
`speech_activity_detection_pyannote.ipynb` detects and plots speech and silences using Pyannote package. You can use recordings in `data/input/audio_samples` to test [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/speech_activity_detection_pyannote.ipynb) 


# Annotations


`annotation.py` takes data from `./data/input/vfp_audios_16khz/` (just the first third of the speech task) dir and outputs a DF in `./data/outputs/annotations/` 

Obtain `vfp_audios_16khz/` cannot be shared. Ask for it. 

After verifying the configuration (paths, instructions, how many seconds to play) in the first few lines, run:

```
pip3 install playsound PyObjC pandas pyaudio
python3 annotation.py
```


### Colab option
`annotation.ipynb` is a Colab approach. when you use `display.display(display.Audio(path))` in Jupyter you can't include a input() in the next line. So this is an alternative approach where all audio files are listed  and one can splitscreen and manually label with a spreadsheet. 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/annotation.ipynb)


