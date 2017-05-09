#!/usr/bin/python

import os
import sys
import shutil
import subprocess

class Create:
    @classmethod

    def run(self, project_name):
        project_directory = Create().getProjectDirectory(project_name)
        if not os.path.exists(project_directory):
            os.makedirs(project_directory)
            if os.path.exists(project_directory):
                project_created_dockercomposeyml = project_directory +'/docker-compose.yml'
                project_created_dockercontrolyml = project_directory +'/dockercontrol.yml'
                Create().createBasedockRepositoryClone(project_directory, project_name)
                Create().replaceBadedockNamespaceString(project_created_dockercomposeyml, project_name)
                Create().replaceBadedockNamespaceString(project_created_dockercontrolyml, project_name)
        else:
            print project_directory +' already exists, choose another name.'

    def getProjectDirectory(self, project_name):
        current_directory = os.path.abspath(os.curdir)
        project_directory = current_directory +'/'+ project_name
        return project_directory

    def createBasedockRepositoryClone(self, project_directory, project_name):
        project_git_folder = project_directory +'/.git'
        project_gitignore_file = project_directory + '/.gitignore'
        project_persistant_storage_directory = project_directory +'/.docker/persistant_storage'
        subprocess.call(['git', 'clone', 'git@gitlab.wklive.net:pixelpiloten/basedock.git', project_name])
        subprocess.call(['rm', '-rf', project_git_folder, project_gitignore_file])
        subprocess.call(['chmod', '-R', '777', project_persistant_storage_directory])

    def replaceBadedockNamespaceString(self, projectfile, project_name):
        with open(projectfile, 'r') as ef:
            replacedlines = []
            oldlines = []
            for line in ef.readlines():
                replacedlines.append(line.replace('basedock', project_name))
                oldlines.append(line)
        with open(projectfile, 'w') as ef:
            for line in replacedlines:
                    ef.write(line)