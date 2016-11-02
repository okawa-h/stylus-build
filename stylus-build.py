#!/usr/bin/env python

import sys
import subprocess

args      = sys.argv
project   = args[1]
targetDir = args[2]

dir = targetDir.split('/')
counter = 0

for file in dir:
	if file == 'src':
		counter += 2
		break
	else :
		counter += 1

for var in xrange(0,counter):
	dir.pop(0)

dir.pop()
dir = '/'.join(dir)
output = project + "/html/" + dir
cmd = ["stylus", "-u", "nib" , targetDir , "--out" , output]
print subprocess.check_output(cmd)
