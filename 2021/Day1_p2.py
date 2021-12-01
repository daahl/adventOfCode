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
sumA: int
sumB: int
for i in range(len(scans_str) - 3): # gives range [0,...,len(scans_str) - 4]
    sumA = int(scans_str[i]) + int(scans_str[i + 1]) + int(scans_str[i + 2])
    sumB = int(scans_str[i + 1]) + int(scans_str[i + 2]) + int(scans_str[i + 3])

    if sumB > sumA:
        increased += 1

print(increased)