ARG ELASTIC_VERSION=8.8.1

FROM docker.elastic.co/logstash/logstash:${ELASTIC_VERSION}

USER root

COPY ./config/pipelines.yml /usr/share/logstash/config/pipelines.yml
COPY ./config/logstash.yml /usr/share/logstash/config/logstash.yml

COPY ./pipeline/dlq.conf /usr/share/logstash/pipeline/dlq.conf
COPY ./pipeline/logstash.conf /usr/share/logstash/pipeline/logges.conf
