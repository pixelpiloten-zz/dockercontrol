#!/usr/bin/python

import subprocess

class Helpers:
    @classmethod

    def getContainerID(self, environment_namespace, container_name):
        container_full_name = environment_namespace + '_' + container_name
        container_details = subprocess.check_output(['docker', 'ps'])
        container_id = ""
        for item in container_details.splitlines():
            if container_full_name in item:
                container_id = item[:12]
                break
        return container_id

    def colorizeOutput(self, label, text):
        color_green = '\033[92m'
        color_gray = '\033[37m'
        return color_green + label +': '+ color_gray + color_gray + text