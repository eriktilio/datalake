# https://www.docker.elastic.co/
ARG ELASTIC_VERSION
FROM docker.elastic.co/elasticsearch/elasticsearch:${ELASTIC_VERSION}
COPY ./config/elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
# Add your elasticsearch plugins setup here
# Example: RUN elasticsearch-plugin install analysis-icu
