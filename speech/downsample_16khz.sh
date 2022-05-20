
input_dir="./data/input/qualitative_interview_2022_02_07_wav/"
output_dir="./data/input/qualitative_interview_2022_02_07_wav_16/" 
files_to_find="*.wav"
downsample_to=16000


mkdir -p $output_dir
for i in $input_dir$files_to_find; do
    o=$output_dir/${i#$input_dir}
    sox "$i" -r $downsample_to "${o%}"
done