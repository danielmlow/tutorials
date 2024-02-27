# Use jupyter in interactive mode on cluster with GPU

Info on using GPUs on OpenMind cluster: 
- https://github.mit.edu/MGHPCC/OpenMind/wiki/How-to-submit-GPU-jobs%3F
- https://github.mit.edu/MGHPCC/OpenMind/wiki/How-to-request-GPUs-with-multiple-CPU-cores-or-nodes%3F 

Figure out what type of GPU you need: `sinfo -p normal -N -o "%f %G"` 

1. Connect to cluster
2. Ask for a GPU

  `srun -N1 -c1 -t 3:00:00 --gres=gpu:1 --constraint=any-gpu --mem=12G --pty bash`

  Or ask for a specific GPU (make sure you use most of the RAM it has and its active most of the time you asked for to avoid issues with future queues):

  `srun -N1 -t 2:00:00 --gres=gpu:QUADRORTX6000:1 --pty bash`

  If you need to load a version of CUDA: `module load openmind8/cuda/12.1`


`srun -N1 -t 2:00:00 --gres=gpu:QUADRORTX6000:1 --pty bash`


  Or run a CPU:

  `srun --pty --nodes=1 --cpus-per-task=10 --time=36:00:00 --mem=10G bash`

3. conda activate `your_virtual_environment_name`


4. Run jupyter

  `jupyter notebook --ip=0.0.0.0 --port=9000 --no-browser`


  This will return a URL which contains a node number and and a token:

  `http://node<node>:9000/lab?token=<token>`

5. Open new terminal and run this command using the node number.


  `ssh -L <host_number>:node<node>:9000 <username>@openmind.mit.edu`
  
  Example: `ssh -L 1333:node080:9000 dlow@openmind.mit.edu`

  You can add a host number like 1333 or a new one if another one is already active. 


6. Open a browser (e.g., Chrome) and type: `http://localhost:<host_number>/`

  Example: `http://localhost:1333`

8. Jupyter will open and ask you for the token.

Check efficiency:
- seff <JobID>





### Other 

Exclude certain nodes: 
`srun -N1 -c10 -t 2:00:00 --gres=gpu:1 --exclude node033,node034,node035,node043,node055,node056,node057,node066 --pty bash`

Obtain priority on labs GPUs: `--partition=gablab`


