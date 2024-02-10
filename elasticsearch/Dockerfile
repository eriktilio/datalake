# Use a imagem oficial do Elasticsearch a partir do Docker Hub com a versão fornecida como argumento.
ARG ELASTIC_VERSION
FROM docker.elastic.co/elasticsearch/elasticsearch:${ELASTIC_VERSION}

# Copie o arquivo de configuração personalizado para o diretório de configuração do Elasticsearch na imagem.
COPY ./config/elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

# Adicione a configuração para instalação de plugins do Elasticsearch.
# Exemplo: RUN elasticsearch-plugin install analysis-icu
