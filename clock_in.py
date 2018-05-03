#!/usr/bin/python3

import sys, re
from datetime import datetime

usage_info = """clock_in <options>
    -t=Time(default = curr time)(format hh:mm:ss)
    -d=Date(default = curr date)(format dd:mm:yy)
    -g=Goal(default = previous goal)
"""

time_in = datetime.now().time()
date_in = datetime.now().date()
goal = "No Goal"
for val in sys.argv[1:]:
    m = re.match("-(.)=(.*)", val)
    if (m):
        if (m.group(1) == 't'):
            try:
                time_in = datetime.strptime(m.group(2), "%H:%M:%S").time()
            except:
                sys.stderr.write("Error not correct time format hh:mm:ss\n")
        elif (m.group(1) == 'd'):
            try:
                date_in = datetime.strptime(m.group(2), "%d/%m/%y").date()
            except:
                sys.stderr.write("Error not correct date format dd:mm:yy\n")

        elif (m.group(1) == 'g'):
            goal = m.group(2)
        else:
            sys.stdout.write(usage_info)
            exit(1)
    else:
        sys.stdout.write(usage_info)
        exit(1)
start = datetime.combine(date_in, time_in).strftime('%Y-%m-%d %H:%M:%S')
sys.stdout.write("Start: " + str(start) + " Goal: " + goal + "\n")

with open("time_in", "a") as f:
    f.write('{}, {}\n'.format(str(start),goal))

