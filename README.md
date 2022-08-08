




# Tutorials
Quick and dirty tutorials and templates 


# Template files
- `template.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/template.ipynb) 
- `template.py`

<br>
# Plotting and input/output in `plotting_and_io/`

## Save static Plotly images in Colab
`save_plotly_colab.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/plotting_and_io/save_plotly_colab.ipynb) 


## dump / load json files
`load_write_json.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/plotting_and_io/load_write_json.ipynb) 



## Rename files 

```
brew install rename
rename 's/cleaned/16khz/' *.wav
```

text
speech
emails_from_python

# Send emails in `emails/`

1. First create a script called `email_config.py` with these variables using your info:

```python
port = 465  #For SSL. eg, 465 
smtp_server = "outgoing.mit.edu" #eg, "outgoing.mit.edu" with the "outgoing" part
from_email_actual = "username"  # actual email sent by. just the username of the above email. eg., "username@mit.edu"
from_email_appears = "other_username@mit.edu"  # It will appeared as sent by this email "other_username@mit.edu" or it could be the same one as from_email_actual. You need authorization to send from other emails which you can configure in your email settings. 
also_send_to = ['username@gmail.com', 'other_username2@mit.edu']  # you can Add email to receive copy or leave empty list, but note some .edu accounts cannot send to themselves. These emails will not be seen by recipient. 
cc = None # This will appear, but note some .edu accounts cannot send to themselves
testing = True #send the emails to the email specified in testing_to_email to test everything is running well and the html formatting looks right. 
testing_to_email = 'daniel.m.low@gmail.com'
testing_append_subject_line = '[Test] '
```

2. `email_content.py` Here you define the email subject line and body of the different types of emails. Use HTML (e.g., `<br>` for line breaks, etc.).

3. Define a CSV file with emails and email_type. This will allow `email_send.py` to call extract certain body and subject lines from `email_content.py`. You will call this csv file in the argument, see below. In my example, include columns `to_email`, `name`, `email_type`, and `prizes`, but you can include whatever you need and change in `email_content.py` accordingly.

4. Run script

This will prompt you for the password of from_email_actual
```
python3 email_send.py --path_to_dataframe=path/to/dataframe.csv
```


# Speech processing in `speech/`

## Convert mp3 to other format
pip3 install pydub
python3 convert_mp3.py --input_dir='data/input/ --output_dir= --output_format=wav --output_bitrate=32k


## Downsample sampling rate 
Most speech occurs below 8kHz. Therefore downsampling to 16kHz is enough to capture most speech-related frequencies and information (see Nyquist rate). Many algorithms require samples to be at 16kHz (for faster processing or normalization across samples) while many recordings are done at 22 or 44kHz.

```
sh downsample_16khz.sh
```


## Automatic speech recognition (ASR)
`asr.ipynb` uses SpeechBrain models 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/speech/asr.ipynb)



## Speech Activity Detection
`speech_activity_detection_pyannote.ipynb` detects and plots speech and silences using Pyannote package. You can use recordings in `data/input/audio_samples` to test [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/speech/speech_activity_detection_pyannote.ipynb) 


## Speech-shaped noise

`speech_shaped_noise.ipynb` As a control for speech. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/speech/speech_shaped_noise.ipynb)


## Extract OpenSmile eGeMAPS features
`extract_opensmile_features.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/speech/extract_opensmile_features.ipynb)





## Annotations

#### Annotations - Colab option
`audio_annotation.ipynb` is a Colab approach. 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/speech/audio_annotation.ipynb)

#### Annotations - CLI option
`audio_annotation.py` takes data from `./data/input/vfp_audios_16khz/` (just the first third of the speech task) dir and outputs a DF in `./data/outputs/annotations/` 

Obtain `vfp_audios_16khz/` cannot be shared. Ask for it. 

After verifying the configuration (paths, instructions, how many seconds to play) in the first few lines, run:

Example:
```
pip3 install playsound PyObjC pandas pyaudio
python3 annotation.py --input_dir=data/input/vfp_audios_16khz/ --output_dir=data/outputs/annotations/ 
```


# Text and NLP processing in `text/`

`sentiment_analysis_emotion.ipynb`
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/text/sentiment_analysis_emotion.ipynb)

`find_closest_word.ipynb`
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/text/find_closest_word.ipynb)



# Machine learing in `machine_learning/`

`classifier.ipynb`
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/danielmlow/tutorials/blob/main/machine_learning/classifier.ipynb)









