#!/usr/bin/python

from Commands.Application import *

class Help:
    @classmethod

    def run(self):
        applications = Application().getApplications()
        color_green = '\033[92m'
        color_gray = '\033[37m'
        print ''
        print color_green + 'up'
        print color_gray + ' Starts the containers.'
        print color_green + 'down'
        print color_gray + ' Stops the containers.'
        print color_green + 'provision'
        print color_gray + ' Provisions the containers.'
        print color_green + 'rebuild'
        print color_gray + ' Stops the containers, gets the latest images and rebuilds them.'
        print color_green + 'ssh'
        print color_gray + ' Get a bash-prompt inside the specified container.'
        print color_green + 'status'
        print color_gray +' Gets the process output of docker containers.'
        if(applications):
            for key, value in applications.items():
                print color_green + key +' (custom command)'
                print color_gray + ' '+ value['description']