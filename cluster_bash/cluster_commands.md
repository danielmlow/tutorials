# checking what happened to past jobs

Add start date. 

`sacct -X -S 2023-01-01` 



# Testing new code on cluster in interactive mode

When testing out new code, it's good to run an interactive node. 

```srun -N1 -c1 -t 3:00:00 --gres=gpu:1 --constraint=any-gpu --mem=12G --pty bash```

Activate virtual env

```conda activate ct```

Then run script in interactive mode, which will likely run a lot slower, but allows one to interact with code:

```python -i script_name.py```





