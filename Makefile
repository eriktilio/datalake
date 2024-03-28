# Makefile para gerenciar comandos Docker Compose

# Nome do arquivo docker-compose.yml
DOCKER_COMPOSE_FILE := docker-compose.yml

.PHONY: help
help: ## Exibe esta mensagem de ajuda
	@echo "Uso: make [target]"
	@echo ""
	@echo "Targets disponíveis:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: up
up: ## Iniciar contêineres Docker Compose
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d

.PHONY: down
down: ## Parar e remover contêineres Docker Compose
	docker compose -f $(DOCKER_COMPOSE_FILE) down

.PHONY: restart
restart: down up ## Reiniciar contêineres Docker Compose

.PHONY: logs
logs: ## Exibir logs dos contêineres Docker Compose
	docker compose -f $(DOCKER_COMPOSE_FILE) logs

.PHONY: ps
ps: ## Exibir status dos contêineres Docker Compose
	docker compose -f $(DOCKER_COMPOSE_FILE) ps

.PHONY: exec
exec: ## Executar comando em um contêiner Docker Compose, use ARGS='nome_do_servico comando'
	docker compose -f $(DOCKER_COMPOSE_FILE) exec $(ARGS)

.PHONY: build
build: ## Construir (ou reconstruir) imagens Docker Compose
	docker compose -f $(DOCKER_COMPOSE_FILE) build

.PHONY: clean
clean: ## Remover volumes Docker Compose não utilizados
	docker compose -f $(DOCKER_COMPOSE_FILE) down --volumes --remove-orphans

.PHONY: remove-images
remove-images: ## Remove todas as imagens associadas ao arquivo docker-compose.yml
	docker compose -f $(DOCKER_COMPOSE_FILE) down --rmi all