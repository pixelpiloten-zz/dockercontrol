#!/usr/bin/python

import subprocess

class Rebuild:
    @classmethod

    def run(self):
        subprocess.check_output(['docker-compose', 'stop'])
        subprocess.check_output(['docker-compose', 'rm', '-f'])
        subprocess.check_output(['docker-compose', 'pull'])
        subprocess.check_output(['docker-compose', 'up', '--build', '-d'])