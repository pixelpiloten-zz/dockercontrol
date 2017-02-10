#!/usr/bin/python

import os;
import sys;
import subprocess;

current_path = os.path.abspath(os.getcwd());
app_name = os.path.basename(current_path); 
command = sys.argv[1];

# Change dir to path where command is run
os.chdir(current_path);

if command == 'up':
	subprocess.check_output(['docker-compose', 'up', '-d']);
elif command == 'down':
	subprocess.check_output(['docker-compose', 'stop']);
elif command == 'provision':
	subprocess.check_output(['docker-compose', 'stop']);
	subprocess.check_output(['docker-compose', 'rm', '-f']);
	subprocess.check_output(['docker-compose', 'up', '--build', '-d']);
elif command == 'rebuild':
	subprocess.check_output(['docker-compose', 'stop']);
	subprocess.check_output(['docker-compose', 'rm', '-f']);
	subprocess.check_output(['docker-compose', 'pull']);
	subprocess.check_output(['docker-compose', 'up', '--build', '-d']);
elif command == 'ssh':
    container_name = app_name +'_'+ sys.argv[2];
    container_details = subprocess.check_output(['docker', 'ps']);
    for item in container_details.splitlines():
        if container_name in item:
            container_id = item[:12];
            subprocess.call(['docker', 'exec', '-i', '-t', container_id, '/bin/bash']);
else:
	print 'Invallid argument!'
