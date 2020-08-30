#!/usr/bin/python3.6

print("Content-Type: text/html\n")

import subprocess

today = subprocess.getoutput("date")

print(today)