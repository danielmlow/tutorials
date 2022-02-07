"""
python3
IMPORTANT. Install:
pip3 install playsound PyObjC pandas 
"""

import os 
import pandas as pd
import numpy as np
import random 
import datetime
from playsound import playsound
import pyaudio
import wave
from scipy.io import wavfile

# config
data_dir = 'vfp_audios_16khz' #used to name the output file as well
input_dir = f'./data/input/{data_dir}/'
output_dir = './data/output/annotations/'
instructions = '1=if volume is very low; 2=normal; 3=gain was likely raised; 99=unsure; r=repeat; q=save and quit. Or instead type in a note here: '
play_n_seconds = 5

# main
# ===========================



def play_partial_sound(path_to_wav, start = 0, play_n_seconds = play_n_seconds):
  # https://stackoverflow.com/questions/18721780/play-a-part-of-a-wav-file-in-python
  # open wave file
  wave_file = wave.open(path_to_wav, 'rb')

  # initialize audio
  py_audio = pyaudio.PyAudio()
  stream = py_audio.open(format=py_audio.get_format_from_width(wave_file.getsampwidth()),
                        channels=wave_file.getnchannels(),
                        rate=wave_file.getframerate(),
                        output=True)

  # skip unwanted frames
  n_frames = int(start * wave_file.getframerate())
  wave_file.setpos(n_frames)

  # write desired frames to audio buffer
  n_frames = int(play_n_seconds * wave_file.getframerate())
  frames = wave_file.readframes(n_frames)
  stream.write(frames)

  # close and terminate everything properly
  stream.close()
  py_audio.terminate()
  wave_file.close()
  return



files = os.listdir(input_dir)
files = [n for n in files if 'Speech_1' in n] #just keep first sample of Speech for each participant
print(len(files), 'files')
print('avg. length 6.8 sec +- 5.4 sec')
print(instructions+'\n')

seed = 123
random.Random(seed).shuffle(files) ## shuffle order of files with seed so that if you quit in the middle, you can continue where you left off
annotation = []
lengths = []
for i, file_i in enumerate(files):
  # get length
  samplerate, data = wavfile.read(input_dir+file_i) 
  length = np.round(data.shape[0]/samplerate,1)
  print(f'======= playing file #{i}, {length} sec ...')
  play_partial_sound(input_dir+file_i, start = 0, play_n_seconds = play_n_seconds)
  # playsound(input_dir+file_i) #play audio
  resp = input(instructions) #record annotation
  if resp == 'r':
    play_partial_sound(input_dir+file_i, start = 0, play_n_seconds = play_n_seconds)
    # playsound(input_dir+file_i)
    resp = input(instructions)
  elif resp == 'q':
    break
  else:
    annotation.append([file_i, resp, ])
  print('\n')

# create DF
annotation = pd.DataFrame(annotation, columns = ['file', 'annotation'])
ts = datetime.datetime.utcnow().strftime('%y-%m-%dT%H-%M-%S')
annotation.to_csv(output_dir+f'annotations_{data_dir}_{ts}.csv')

