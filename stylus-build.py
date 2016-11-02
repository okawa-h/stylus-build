# -*- coding: utf-8 -*-

import os.path
import sys
import subprocess

def getProjectName(projectDir):
	dir = projectDir.split('/')
	return dir[len(dir)-1]

def getDirectory(targetFile,projectName):
	dir  = targetFile.split('/')
	dir.pop()
	flag = False
	directory = []
	for file in dir:
		if flag:
			directory.append(file)
		if file == projectName:
			flag = True
	directory.pop(0)
	directory.pop(0)
	return '/'.join(directory)

args        = sys.argv
projectDir  = args[1]
targetFile  = args[2]
targetDir   = args[3]
outputDir   = args[4]
projectName = getProjectName(projectDir)
directory   = getDirectory(targetFile,projectName)

output = projectDir + "/" + outputDir + directory

if os.path.isdir(output):
	cmd = ["stylus", "-u", "nib" , targetFile , "--out" , output]
	print subprocess.check_output(cmd)
else:
	print output + '\nディレクトリがありません🐘'


