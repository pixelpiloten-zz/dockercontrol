#!/usr/bin/python

import os;
import sys;
import subprocess;

current_path = os.path.abspath(os.getcwd());
app_name = os.path.basename(current_path); 
argument = sys.argv[1];

# Change dir to path where command is run
os.chdir(current_path);

if argument == 'up':
	subprocess.check_output(['docker-compose', 'up', '-d']);
elif argument == 'down':
	subprocess.check_output(['docker-compose', 'stop']);
elif argument == 'provision':
	subprocess.check_output(['docker-compose', 'stop']);
	subprocess.check_output(['docker-compose', 'rm', '-f']);
	subprocess.check_output(['docker-compose', 'up', '--build', '-d']);
elif argument == 'rebuild':
	subprocess.check_output(['docker-compose', 'stop']);
	subprocess.check_output(['docker-compose', 'rm', '-f']);
	subprocess.check_output(['docker-compose', 'pull']);
	subprocess.check_output(['docker-compose', 'up', '--build', '-d']);
else:
	print 'Invallid argument!'
