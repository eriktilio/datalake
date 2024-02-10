# Use a imagem base do Logstash especificando a versão desejada
ARG ELASTIC_VERSION
FROM docker.elastic.co/logstash/logstash:${ELASTIC_VERSION}

# Defina o usuário como root para realizar operações necessárias
USER root

# Copie os arquivos de configuração e pipelines para o diretório apropriado
COPY ./config/pipelines.yml /usr/share/logstash/config/pipelines.yml
COPY ./config/logstash.yml /usr/share/logstash/config/logstash.yml
COPY ./jars/ /usr/share/logstash/logstash-core/lib/jars

# Copie os arquivos de pipeline para o diretório apropriado
COPY ./pipeline/dlq.conf /usr/share/logstash/pipeline/dlq.conf
COPY ./pipeline/logges.conf /usr/share/logstash/pipeline/logges.conf
COPY ./pipeline/client_opcua.conf /usr/share/logstash/pipeline/client_opcua.conf
COPY ./pipeline/mysql_database.conf /usr/share/logstash/pipeline/mysql_database.conf

# Crie o diretório para a Dead Letter Queue e garanta as permissões adequadas
RUN mkdir -p /usr/share/logstash/data/dead_letter_queue
RUN chown -R logstash:logstash /usr/share/logstash/data/dead_letter_queue

# Instale os plugins
RUN bin/logstash-plugin install logstash-output-exec
RUN bin/logstash-plugin install logstash-input-http
#RUN bin/logstash-plugin install logstash-input-jdbc -> você não precisa instalar caso Logstash maior que (7.x)