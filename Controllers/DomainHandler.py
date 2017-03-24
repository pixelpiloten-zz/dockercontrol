#!/usr/bin/python

from Controllers.Helpers import *
import subprocess
import simplejson as json
from python_hosts import Hosts, HostsEntry

class DomainHandler:

    def setEtcHostnames(self, environment_namespace):
        all_running_containers_in_namespace = Helpers().getAllRunningContainersInNamespace(environment_namespace)
        etc_hosts = Hosts()
        for container_row in all_running_containers_in_namespace:
            container_id = container_row[:12]
            container_info = self.getContainerInfo(container_id)
            container_name = self.getContainerName(container_info)
            network_name = self.getEnvironmentNetworkName(environment_namespace)
            container_ip = self.getContainerIpAddress(container_info, network_name)
            if container_ip:
                container_hostname = self.resolveContainerDomainName(environment_namespace, container_name)
                etc_hosts_entry = HostsEntry(entry_type='ipv4', address=container_ip, names=[container_hostname])
                etc_hosts.add([etc_hosts_entry])
        if etc_hosts.count() > 0:
            etc_hosts.write()
            print 'Adding hostname(s) to /etc/hosts.'

    def removeEtcHostnames(self, environment_namespace):
        all_running_containers_in_namespace = Helpers().getAllRunningContainersInNamespace(environment_namespace)
        etc_hosts = Hosts()
        for container_row in all_running_containers_in_namespace:
            container_id = container_row[:12]
            container_info = self.getContainerInfo(container_id)
            container_name = self.getContainerName(container_info)
            container_hostname = self.resolveContainerDomainName(environment_namespace, container_name)
            etc_hosts.remove_all_matching(name=container_hostname)
        etc_hosts.write()
        print 'Removing hostname(s) from /etc/hosts.'

    def getContainerInfo(self, container_id):
        container_info_json = subprocess.check_output(['docker', 'inspect', container_id])
        return json.loads(container_info_json)[0]

    def getContainerName(self, container_info):
        return container_info['Name'].replace('/', '')

    def getEnvironmentNetworkName(self, environment_namespace):
        return environment_namespace +'_default'

    def getContainerIpAddress(self, container_info, network_name):
        if network_name in container_info['NetworkSettings']['Networks']:
            container_ip = container_info['NetworkSettings']['Networks'][network_name]['IPAddress']
        else:
            container_ip = None
        return container_ip

    def resolveContainerDomainName(self, environment_namespace, container_name):
        container_name_split = container_name.split('_')
        container_base_name = container_name_split[1]
        return container_base_name +'.'+ environment_namespace +'.docker'