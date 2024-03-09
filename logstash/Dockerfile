# Use a imagem base do Logstash especificando a versão desejada
ARG ELASTIC_VERSION
FROM docker.elastic.co/logstash/logstash:${ELASTIC_VERSION}

# Defina o usuário como root para realizar operações necessárias
USER root

# Copie os arquivos de configuração e pipelines para o diretório apropriado
COPY ./config /usr/share/logstash/config
COPY ./files /files

# Copie os arquivos de pipeline para o diretório apropriado
COPY ./pipeline /usr/share/logstash/pipeline

# Crie o diretório para a Dead Letter Queue e garanta as permissões adequadas
RUN mkdir -p /usr/share/logstash/data/dead_letter_queue
RUN chown -R logstash:logstash /usr/share/logstash/data/dead_letter_queue

# Instale os plugins
RUN bin/logstash-plugin install logstash-output-exec
RUN bin/logstash-plugin install logstash-input-http
#RUN bin/logstash-plugin install logstash-input-jdbc -> você não precisa instalar caso Logstash maior que (7.x)