
If the file is already there, then ignore (don't try to copy) and move to the next file (change <user> and path)

`rsync --verbose -a --ignore-existing /absolute/path/to/dir/ <user>@openmind.mit.edu:/path/to/dir/`

Or this to move everything even if it already exists remotely:

`scp -r source destination`
