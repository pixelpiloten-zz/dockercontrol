#!/usr/bin/python

import os
import sys

from Controllers.Up import Up
from Controllers.Down import Down
from Controllers.Provision import Provision
from Controllers.Rebuild import Rebuild
from Controllers.Ssh import Ssh
from Controllers.Status import Status
from Controllers.Help import Help

current_path = os.path.abspath(os.getcwd())
app_name = os.path.basename(current_path)

# Change dir to path where command is run
os.chdir(current_path)

if len (sys.argv) > 1:
    command = sys.argv[1]
    if sys.argv[1] == 'up':
        Up.run()
    elif sys.argv[1] == 'down':
        Down.run()
    elif sys.argv[1] == 'provision':
        Provision.run()
    elif sys.argv[1] == 'rebuild':
        Rebuild.run()
    elif sys.argv[1] == 'ssh':
        Ssh.run(app_name)
    elif sys.argv[1] == 'status':
        Status.run(app_name)
    elif sys.argv[1] == 'help':
        Help.run()
    else:
        print 'There is no command like that!'
else:
    Help.run()