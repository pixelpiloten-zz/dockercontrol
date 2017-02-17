#!/usr/bin/python

import subprocess
import sys
from Controllers.Helpers import *

class Ssh:
    @classmethod

    def run(self, app_name):
        if sys.argv[2]:
            container_id = Helpers.getContainerID(app_name, sys.argv[2])
            subprocess.call(['docker', 'exec', '-i', '-t', container_id, '/bin/bash'])
        else:
            print 'You must provide a container-name.'