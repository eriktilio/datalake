#!/bin/bash

# Construir a imagem Docker
docker build -t my-database-mysql .

# Executar o container com o Flyway
docker run -p 3306:3306 my-database-mysql