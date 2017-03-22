#!/usr/bin/python

import subprocess
from Controllers.DomainHandler import *

class Down:
    @classmethod

    def run(self, environment_namespace):
        DomainHandler().removeEtcHostnames(environment_namespace)
        subprocess.check_output(['docker-compose', 'stop'])