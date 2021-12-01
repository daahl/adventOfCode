# thanks to Martijn Pieters on https://www.py4u.net/discuss/151781 for these three rows
# because working with file systems is difficult...
import os
here: str = os.path.dirname(os.path.abspath(__file__))
filename: str = os.path.join(here, 'Day1_inputs.txt')

# read file contents
with open(filename) as scans_file:
    scans_str: str = scans_file.readlines()

# check for increasing lengths
increased: int = 0
for i in range(1, len(scans_str)): # gives range [1,...,len(scans_str) - 1]
    if int(scans_str[i]) > int(scans_str[i - 1]):
        increased += 1

print(increased)