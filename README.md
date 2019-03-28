# CS 6476 project 6: [Deep Learning](https://www.cc.gatech.edu/~hays/compvision/proj6/)

# Setup
- Install [Miniconda](https://conda.io/miniconda). It doesn't matter whether you use 2.7 or 3.6 because we will create our own environment anyways.
- Create a conda environment, using the appropriate command. On Windows, open the installed "Conda prompt" to run this command. On MacOS and Linux, you can just use a terminal window to run the command. Modify the command based on your OS ('linux', 'mac', or 'win'): `conda env create -f environment_<OS>.yml`
- This should create an environment named `cs6476p6`. Activate it using the following Windows command: `activate cs6476p6` or the following MacOS / Linux command: `source activate cs6476p6`.
- Run the notebook using: `jupyter notebook ./code/proj6.ipynb`
- Generate the submission once you're finished using `python zip_submission.py`

# My Setup
- it should be doable in vanilla notebook file, as long as RGB setting below is followed
- For part 1, I set RGB=False
- For part 2, I set RGB=True
- I put another file called "code/just_in_case_files_in_logs_do_not_work" just in case models in logs do not work. But I did train models on CPU on last run, so should work.
- FYI, torchsummary.summary does not seem to work on CPU.

# Extra_Credit
- proj6-exp_sketch.ipynb is the notebook I used for extra credit.
- I only used GPU for this task, else it would take a long time.
- The dataset I modified to use: https://drive.google.com/file/d/1BGuJEFIsaaMsr_JmDik0HnnHVlgWbpnX/view?usp=sharing
- ignore code/split_sketch.py: I used it to split dataset, but have to comment and comment some lines to do so each run.