#!/usr/bin/env python

# Python 3.9.5

# 00_introduction.py

# Dependency
import subprocess

path = 'C:\\Windows\\System32\\calc.exe'

process = subprocess.Popen(path, shell=True)
