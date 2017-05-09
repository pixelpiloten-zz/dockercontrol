#!/usr/bin/python

import subprocess
import os

class Build:
    @classmethod

    def run(self, current_path, environment_namespace):
        subprocess.call(['docker-compose', 'stop'])
        subprocess.call(['docker-compose', 'rm', '-f'])

        local_docker_directory = current_path +'/.docker/dockerfiles'

        dockerfile_source_folders = os.listdir(local_docker_directory)
        for folder in dockerfile_source_folders:
            container_name = environment_namespace +'_'+ folder
            dockerfile_location = local_docker_directory +'/'+ folder
            subprocess.call(['docker', 'build', '-t', container_name, dockerfile_location])