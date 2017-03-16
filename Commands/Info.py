#!/usr/bin/python

from Controllers.Helpers import *
import json
import subprocess

class Info:
    @classmethod

    def getSingleContainerInfo(self, environment_namespace, container_name):
        Info().getContainerInfoByName(environment_namespace, container_name)

    def getAllContainersInfo(self, environment_namespace):
        all_running_containers = subprocess.check_output(['docker', 'ps'])
        containers_namespace = environment_namespace +'_'
        for item in all_running_containers.splitlines():
            if containers_namespace in item:
                self.getContainerInfoByID(item[:12])

    def getContainerInfoByName(self, environment_namespace, container_name):
        container_id = Helpers.getContainerID(environment_namespace, container_name)
        self.printContainerInfo(container_id)

    def getContainerInfoByID(self, container_id):
        self.printContainerInfo(container_id)

    def printContainerInfo(self, container_id):
        container_info_json = subprocess.check_output(['docker', 'inspect', container_id])
        container_info = json.loads(container_info_json)[0]
        print ''
        container_full_name = container_info['Name'].replace('/', '')
        print Helpers().colorizeOutput('Name', container_full_name)
        print Helpers().colorizeOutput('Container ID', container_id)
        print Helpers().colorizeOutput('Created', container_info['Created'])
        print Helpers().colorizeOutput('Ports', '')
        for key, value in container_info['HostConfig']['PortBindings'].items():
            print ' - '+ key
        print Helpers().colorizeOutput('Hostname(s)', '')
        if container_info['HostConfig']['ExtraHosts'] is not None:
            for hostname in container_info['HostConfig']['ExtraHosts']:
                print ' - '+ hostname
        print Helpers().colorizeOutput('Mount(s)', '')
        for mount in container_info['Mounts']:
            print ' - '+ mount['Source'] +' -> '+ mount['Destination']
        print ''