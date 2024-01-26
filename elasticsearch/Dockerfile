ARG ELASTIC_VERSION=8.8.1
# https://www.docker.elastic.co/
FROM docker.elastic.co/elasticsearch/elasticsearch:${ELASTIC_VERSION}
COPY ./config/elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
# Add your elasticsearch plugins setup here
# Example: RUN elasticsearch-plugin install analysis-icu
