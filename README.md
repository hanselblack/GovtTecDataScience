# Attempt
I was attempting this challenge after the Data Engineering Challenge, hence time constraint was a factor.
Nevertheless, it was fun doing this challenge!

I have added 2 columns into the excel data, the duration between Origin and Destination in hh:mm:ss format
and in seconds format. The seconds column was generated using the formula "“=RC[-1]*86400" which turns hh:mm:ss into seconds.

# Juypter
To run the notebook files, but there are the same code base as the .py file.
```shell
pip install notebook
jupyter notebook
```

## Usage
Run using python 3
```shell
python3 analysis.py
```

This will generate out the output.txt which shows the grouping of the duration of the time.