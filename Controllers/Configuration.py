#!/usr/bin/python

import os
import yaml

class Configuration:
    @classmethod

    def currentPath(self):
        self.current_path = os.path.abspath(os.getcwd())
        return self.current_path

    def environmentNamespace(self):
        return os.path.basename(self.current_path)

    def environmentConfiguration(self):
        configuration_file = self.current_path +'/dockercontrol.yml'
        configuration = None
        if(os.path.exists(configuration_file)):
            with open(configuration_file, 'r') as stream:
                configuration = yaml.load(stream)
        return configuration