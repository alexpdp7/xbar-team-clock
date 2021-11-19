#!/usr/bin/env python3
import subprocess
import sys

print("Team clock")
print("---")

with open(sys.argv[1]) as f:
    for l in f.readlines():
        if l.startswith("#") or not l.strip():
            continue
        who, where = l.strip().split(";")
        time = subprocess.check_output(["date",  "+%A %H:%M"], encoding="utf8", env={"TZ": where}).strip()
        print(time, who, where)
