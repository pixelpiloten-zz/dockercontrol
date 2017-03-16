#!/usr/bin/python

import subprocess
from Controllers.Configuration import *
from Controllers.Helpers import *

class Application:
    @classmethod

    def __init__(self):
        self.configuration = Configuration().environmentConfiguration()

    def getApplications(self):
        applications = None
        if(self.configuration):
            applications = self.configuration['commands']
        return applications

    def runApplication(self, application_name, input_arguments):
        applications = self.getApplications()
        environment_namespace = Configuration().environmentNamespace()
        if application_name in applications:
            application = applications[application_name]
            container_id =  Helpers.getContainerID(environment_namespace, application['container'])

            # Here we remove the 3 first arguments which is path to dockercontrol, dockercontrol-command and
            # application_name, which we dont need.
            input_arguments.pop(0)
            input_arguments.pop(0)
            input_arguments.pop(0)

            base_command = ['docker', 'exec', container_id, command_running_path, application['path']]
            app_config_arguments = application['arguments']
            command = base_command + app_config_arguments  + input_arguments
            subprocess.call(command)
