




# Tutorials
Quick and dirty tutorials and templates 


# dump / load json files
`load_write_json.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/load_write_json.ipynb) 

# Convert mp3 to other format
pip3 install pydub
python3 convert_mp3.py --input_dir='data/input/ --output_dir= --output_format=wav --output_bitrate=32k


# Downsample sampling rate 
Most speech occurs below 8kHz. Therefore downsampling to 16kHz is enough to capture most speech-related frequencies and information (see Nyquist rate). Many algorithms require samples to be at 16kHz (for faster processing or normalization across samples) while many recordings are done at 22 or 44kHz.

```
sh downsample_16khz.sh
```


# Automatic speech recognition (ASR)
`asr.ipynb` uses SpeechBrain models 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/asr.ipynb)



# Speech Activity Detection
`speech_activity_detection_pyannote.ipynb` detects and plots speech and silences using Pyannote package. You can use recordings in `data/input/audio_samples` to test [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/speech_activity_detection_pyannote.ipynb) 


# Annotations
`annotation.py` takes data from `./data/input/vfp_audios_16khz/` (just the first third of the speech task) dir and outputs a DF in `./data/outputs/annotations/` 

Obtain `vfp_audios_16khz/` cannot be shared. Ask for it. 

After verifying the configuration (paths, instructions, how many seconds to play) in the first few lines, run:

Example:
```
pip3 install playsound PyObjC pandas pyaudio
python3 annotation.py --input_dir=data/input/vfp_audios_16khz/ --output_dir=data/outputs/annotations/ 
```


#### Annotations - Colab option
`annotation.ipynb` is a Colab approach. 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/annotation.ipynb)


# Rename files

```
brew install rename
rename 's/cleaned/16khz/' *.wav
```


# Speech-shaped noise

`speech_shaped_noise.ipynb` As a control for speech. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/speech_shaped_noise.ipynb)


# Extract OpenSmile eGeMAPS features
`extract_opensmile_features.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/extract_opensmile_features.ipynb)



