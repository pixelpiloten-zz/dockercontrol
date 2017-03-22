#!/usr/bin/python

import subprocess
from Controllers.DomainHandler import *

class Up:
    @classmethod

    def run(self, environment_namespace):
        subprocess.check_output(['docker-compose', 'up', '-d'])
        DomainHandler().setEtcHostnames(environment_namespace)
