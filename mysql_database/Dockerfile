# Use uma imagem base do MySQL
FROM mysql:8.3.0

# Define variáveis de ambiente para o MySQL
ENV MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
ENV MYSQL_DATABASE=${MYSQL_DATABASE}
ENV MYSQL_USER=${MYSQL_USER}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}

# Copia os scripts SQL para a pasta /docker-entrypoint-initdb.d/ para que sejam executados na criação do container
COPY migrations/ /docker-entrypoint-initdb.d/
