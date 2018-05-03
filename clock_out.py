#!/usr/bin/python3

import sys, re, os
from datetime import datetime

usage_info = """clock_out <options>
    -t=Time(default = curr time)(format hh:mm:ss)
    -d=Date(default = curr date)(format dd:mm:yy)
    -w=Work(default = previous goal)
"""

try:
    with open("time_in", "r") as start_time:
        start_data = start_time.readline()
except:
    sys.stderr.write("No start time file found\n")
    exit(1)

vals = [val.strip() for val in start_data.split(',')]
start = str(datetime.strptime(vals[0], "%Y-%m-%d %H:%M:%S"))
goal = vals[1]

time_out = datetime.now().time()
date_out = datetime.now().date()
work_done = goal
for val in sys.argv[1:]:
    m = re.match("-(.)=(.*)", val)
    if (m):
        if (m.group(1) == 't'):
            try:
                time_out = datetime.strptime(m.group(2), "%H:%M:%S").time()
            except:
                sys.stderr.write("Error not correct time format hh:mm:ss\n")
        elif (m.group(1) == 'd'):
            try:
                date_out = datetime.strptime(m.group(2), "%d/%m/%y").date()
            except:
                sys.stderr.write("Error not correct date format dd:mm:yy\n")
        elif (m.group(1) == 'w'):
             work_done = m.group(2)
        else:
            sys.stdout.write(usage_info)
            exit(1)
    else:
        sys.stdout.write(usage_info)
        exit(1)
end = datetime.combine(date_out, time_out).strftime('%Y-%m-%d %H:%M:%S')
sys.stdout.write("Start: " + str(start) + " Goal: " + goal + " End: " + str(end) + " Work: " + work_done + "\n")

with open("hours", "a") as f:
    f.write('{}, {}, {}, {}\n'.format(str(start),goal,str(end),work_done))

os.remove("./time_in")
