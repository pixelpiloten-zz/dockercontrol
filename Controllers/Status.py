#!/usr/bin/python

import subprocess

class Status:
    @classmethod

    def run(self, app_name):
        container_details = subprocess.check_output(['docker', 'ps'])
        app_containers_output = ""
        global_containers_output = ""
        for item in container_details.splitlines():
            if app_name in item:
                app_containers_output = item +"\n"+ app_containers_output

        if not app_containers_output:
            for item in container_details.splitlines():
                if "CONTAINER ID" not in item:
                    global_containers_output = item + "\n" + global_containers_output

        if app_containers_output:
            print app_containers_output
        elif global_containers_output:
            print global_containers_output
        else:
            print "No running docker containers!"

