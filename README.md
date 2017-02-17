# Install instructions
1. Copy the dockercontrol-folder to `/usr/local/bin/dockercontrol`.
2. Add `/usr/local/bin/dockercontrol` to your `$PATH`.
3. Run `dockercontrol help` to make sure that its working.

# Usage
Tool to control a docker-compose setup (vagrant-style), run in the same folder as your docker-compose file. 

# Commands

> dockercontrol up

Starts the containers.
 
> dockercontrol down

Stops the containers.

> dockercontrol provision

Provisions the containers.

> dockercontrol rebuild

Stops the containers, gets the latest images from registry and rebuilds the containers.

> dockercontrol ssh containername

Get a bash-prompt inside the specified container, use the containername that is specified in the docker-compose file.

> dockercontrol status

Gets the process output of the docker containers, if in the same folder as docker-compose we'll try to get only theese containers, otherwise we will get all running containers.

> dockercontrol info

Gets a short summary about the runing containers in the docker-composer-file, if name of container is provided as a second argument info about only that running container is printed.