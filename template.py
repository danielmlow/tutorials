import pandas as pd
import numpy as np
import os
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Convert all mp3 in input_dir to other format such as wav')
# Add an argument
parser.add_argument('--input_dir', type=str, required=True)
parser.add_argument('--output_dir', type=str, required=True)
parser.add_argument('--output_format', type=str,default='wav')
parser.add_argument('--output_bitrate', type=str,default='32k')

# Parse the argument
args = parser.parse_args()
input_dir = args.input_dir
output_dir = args.output_dir
output_format = args.output_format
output_bitrate = args.output_bitrate


def convert_mp3(input_path, output_path, output_format = 'wav', output_bitrate="32k"):
    # do something
    pass
    return

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
    for n in files:
        convert_mp3(input_dir+n,output_dir+n[:-3]+output_format, output_format=output_format )


