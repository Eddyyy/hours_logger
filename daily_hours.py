#!/usr/bin/python3

import sys, re
from datetime import datetime

try:
    with open("hours", "r") as hours_time:
        hours_data = hours_time.readlines()
except:
    sys.stderr.write("No hours file found\n")
    exit(1)

for line in hours_data:
    vals = [val.strip() for val in line.split(',')]
    start = datetime.strptime(vals[0], "%Y-%m-%d %H:%M:%S")
    goal = vals[1]
    end = datetime.strptime(vals[2], "%Y-%m-%d %H:%M:%S")
    work = vals[3]
    
    sys.stdout.write("Start: " + str(start) + " End: " + str(end) + "\n")
    hours_completed = str(end-start)
    sys.stdout.write("Total Hours: " + hours_completed + "\n")
    sys.stdout.write("Goal-->Work: " + goal + " --> " +  work + "\n")
