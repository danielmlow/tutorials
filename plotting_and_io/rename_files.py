
# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def rename_files(path_to_dir='./', old_str = '.wav', new_str = '_16khz.wav'):
	for count, filename in enumerate(os.listdir(path_to_dir)):
		src =f"{path_to_dir}/{filename}"  # foldername/filename, if .py file is outside folder
		new_filename = filename.replace(old_str,new_str)
		dst =f"{path_to_dir}/{new_filename}"
		# rename() function will rename all the files
		os.rename(src, dst)
	return


# rename files
rename_files(path_to_dir='./',
             old_str = '.wav',
             new_str = '_16khz.wav'
             )