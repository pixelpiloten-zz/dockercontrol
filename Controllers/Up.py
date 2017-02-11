#!/usr/bin/python

import subprocess

class Up:
    @classmethod

    def run(self):
        subprocess.check_output(['docker-compose', 'up', '-d'])