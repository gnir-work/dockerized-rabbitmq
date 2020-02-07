POETRY_EXPORT_COMMAND=poetry export -f requirements.txt --without-hashes > requirments.txt
STACK_NAME=dockerized-rabbitmq
IP_ADDRESS=hostname -I | awk '{print $$1}'

deploy: build init_swarm
	docker stack deploy -c ./docker-compose.yml $(STACK_NAME)

remove_services:
	docker stack down $(STACK_NAME)

list_services:
	docker stack services $(STACK_NAME)

init_swarm: leave_swarm
	docker swarm init --advertise-addr `$(IP_ADDRESS)`

leave_swarm:
	# The pipe true is here in order to ignore the case when we are not part of a swarm
	docker swarm leave --force | true

develop: build
	docker-compose up --build --force-recreate

build: build_worker build_distributer

build_distributer: create_distributer_requirements
	docker build -t distributer distributer

build_worker: create_worker_requirements
	docker build -t worker worker

create_distributer_requirements:
	cd distributer && $(POETRY_EXPORT_COMMAND)

create_worker_requirements:
	cd worker && $(POETRY_EXPORT_COMMAND)
