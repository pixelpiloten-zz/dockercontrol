#!/usr/bin/python

import os

class Configuration:
    @classmethod

    def currentPath(self):
        self.current_path = os.path.abspath(os.getcwd())
        return self.current_path

    def appName(self):
        return os.path.basename(self.current_path)