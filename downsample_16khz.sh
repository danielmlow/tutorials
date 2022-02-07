
input_dir="./data/input/audio_samples_48khz/"
output_dir="./data/input/audios_16khz/" 
files_to_find="*.wav"
downsample_to=16000


mkdir -p $output_dir
for i in $input_dir$files_to_find; do
    o=$output_dir/${i#$input_dir}
    sox "$i" -r $downsample_to "${o%}"
done