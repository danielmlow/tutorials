
Deep learning models are working really well for speech to text and speaker separation (diarization).

## Free, open source models that run on your private computer:
Will run much faster on GPU or but whisper 'small' model or smaller can run on decent CPUs:
- https://github.com/m-bain/whisperX

You can replace the diarization with pyannote, which runs locally, but pyannote-audio requires you to accept their terms and conditions from here, and the way they authenticate you is though the huggingface tokens:
https://github.com/pyannote/pyannote-audio?tab=readme-ov-file#tldr

## Run on a cloud GPU (faster, but for a small cost)
If you can submit data to a companies cloud service, options are:
- https://pyannote.ai/
- https://www.assemblyai.com/docs/speech-to-text/speaker-diarization
- https://cloud.google.com/speech-to-text/docs/multiple-voices#speech_transcribe_diarization_beta-python

## Human editing
Other services like https://www.transcribeme.com/ which can include human editing tend to be more expensive and not that much better. 



