import assemblyai as aai
import os

aai.settings.api_key = "d95fd49cfae34c09a0ef480bc7ad1210"

input_dir = '/Users/danielmlow/code/tutorials/data/input/audio_samples/'
files = os.listdir(input_dir)
files = [n for n in files if n[-3:] == 'mp3']


for n in files:
    audio_file = input_dir+n

    config = aai.TranscriptionConfig(
    speaker_labels=True,
    )

    transcript = aai.Transcriber().transcribe(audio_file, config)

    for utterance in transcript.utterances:
        # save transcript as txt, if it exists, append
        with open(f'/Users/danielmlow/code/tutorials/data/output/assemblyai/{n[:-3]}txt', 'a') as f:
            f.write(print(f"Speaker {utterance.speaker}: {utterance.text}"))
            