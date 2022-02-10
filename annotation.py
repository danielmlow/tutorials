"""
python3
IMPORTANT. Install:
pip3 install playsound PyObjC pandas pyaudio
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
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Annotate files in input_dir according to your instructios argument and output a csv. Filenames are not shown to not bias annotator. Files are in random order, but always the same so you can continue where you left off after saving. ')
# Add an argument
parser.add_argument('--input_dir', type=str, required=True, help = 'for instance: data/input/audios_16khz/')
parser.add_argument('--output_dir', type=str, required=True, help = 'will create if doesnt exist, for instance: data/output/annotations/')
parser.add_argument('--filter', type=str, default=None, help = 'keep files that include this string, for instance: Speech_1')
parser.add_argument('--instructions', type=str,default='1=if volume is very low; 2=normal; 3=gain was likely raised; 99=unsure; r=repeat; q=save and quit. Or instead type in a note here:', help='default is: 1=if volume is very low; 2=normal; 3=gain was likely raised; 99=unsure; r=repeat; q=save and quit. Or instead type in a note here:')
parser.add_argument('--play_n_seconds', type=int,default=5, help='int to pay int sec or 0 to play full, play first n seconds in case files are long. Default is 5.')
parser.add_argument('--continue_from_file_n', type=int,default=0, help='if you already labelled n files and saved the annotation, continue from there.')


# Parse the argument
args = parser.parse_args()
input_dir = args.input_dir
output_dir = args.output_dir
filter = args.filter
print(filter)
print(type(filter))
instructions = args.instructions
play_n_seconds = args.play_n_seconds
continue_from_file_n = args.continue_from_file_n

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


def play_and_get_response(file_i,i, instructions=None, play_n_seconds=None, length=None):
  # recursive function
    if play_n_seconds: 
        # play partial
        print(f'======= file #{i}, {length} sec, playing first {play_n_seconds} sec ...')
        play_partial_sound(input_dir+file_i, start = 0, play_n_seconds = play_n_seconds)
    else:
        # play full
        print(f'======= playing file #{i}, {length} sec ...')
        playsound(input_dir+file_i) #play audio
    resp = input(instructions) #record annotation
    if resp != 'r':
        return resp
    else:
      return play_and_get_response(file_i,i, instructions=instructions, play_n_seconds=play_n_seconds, length=length)

    



if __name__ == '__main__':
    
    try:
        os.mkdir(output_dir)
    except:
        pass
    
    files = os.listdir(input_dir)
    try: 
            files.remove('.DS_Store')
    except:
        pass
    if filter:
      files = [n for n in files if filter in n] #just keep first sample of Speech for each participant
    
    if continue_from_file_n:
      files = files[continue_from_file_n:]
    
    print(len(files), 'files')
    # print('avg. length 6.8 sec +- 5.4 sec')
    print(instructions+'\n')

    seed = 123
    random.Random(seed).shuffle(files) ## shuffle order of files with seed so that if you quit in the middle, you can continue where you left off
    
    annotation = []
    lengths = []
    for i, file_i in enumerate(files):
      if continue_from_file_n:
        i+=continue_from_file_n
      # get length
      samplerate, data = wavfile.read(input_dir+file_i) 
      length = np.round(data.shape[0]/samplerate,1)
      resp = play_and_get_response(file_i,i, instructions=instructions, play_n_seconds=play_n_seconds, length=length)
      if resp == 'q':
        break
      else:
        annotation.append([i, file_i, resp, ])
      print('\n')

    # create DF
    annotation = pd.DataFrame(annotation, columns = ['i','file', 'annotation'])
    ts = datetime.datetime.utcnow().strftime('%y-%m-%dT%H-%M-%S')
    output_filename = input_dir.split('/')[-2] 
    annotation.to_csv(output_dir+f'annotations_{output_filename}_{ts}.csv')
    
    


