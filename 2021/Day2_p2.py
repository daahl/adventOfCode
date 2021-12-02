# thanks to Martijn Pieters on https://www.py4u.net/discuss/151781 for these three rows
# because working with file systems is difficult...
import os
here: str = os.path.dirname(os.path.abspath(__file__))
filename: str = os.path.join(here, 'Day2_inputs.txt')

# read file contents
with open(filename) as scans_file:
    scans_str: str = scans_file.readlines()

horizPos: int = 0
depthPos: int = 0
aim: int = 0

# we actually only care about the first and last char of each element...
# ...as the commands have a unique starting letter...
# ...and the units to move always comes last (but before a "\n")
for s in scans_str:
    if s[0] == "f":
        horizPos += int(s[-2])
        depthPos += int(s[-2]) * aim
    elif s[0] == "u":
        aim -= int(s[-2])
    elif s[0] == "d":
        aim += int(s[-2])
        

print(horizPos * depthPos)  