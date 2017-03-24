#!/usr/bin/python

import subprocess
from Commands.Down import *
from Commands.Up import *

class Restart:
    @classmethod

    def run(self, environment_namespace):
        Down().run(environment_namespace)
        Up().run(environment_namespace)
