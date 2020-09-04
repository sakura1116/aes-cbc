DOCKER_COMPOSE := docker-compose -f docker-compose.yml

docker_run:
	$(DOCKER_COMPOSE) up -d

docker_ssh:
	$(DOCKER_COMPOSE) exec aescbc /bin/bash

py_test:
	$(MAKE) -C src test
