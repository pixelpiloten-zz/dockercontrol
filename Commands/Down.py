#!/usr/bin/python

import subprocess

class Down:
    @classmethod

    def run(self):
        subprocess.check_output(['docker-compose', 'stop'])