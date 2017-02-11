#!/usr/bin/python

import subprocess
import sys

class Ssh:
    @classmethod

    def run(self, app_name):
        container_name = app_name + '_' + sys.argv[2]
        container_details = subprocess.check_output(['docker', 'ps'])
        for item in container_details.splitlines():
            if container_name in item:
                container_id = item[:12]
                subprocess.call(['docker', 'exec', '-i', '-t', container_id, '/bin/bash'])