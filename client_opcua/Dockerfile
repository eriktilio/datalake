# Use uma imagem base do Python 3.11 slim do Docker Hub.
FROM python:3.11-slim

# Define o diretório de trabalho para /opt/client_opcua/.
WORKDIR /opt/client_opcua/

# Copia o arquivo requirements.txt para o diretório de trabalho.
COPY requirements.txt .

# Instala as dependências listadas no requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do contexto de build (diretório local) para o diretório de trabalho na imagem.
COPY . .

# Define o comando padrão a ser executado quando o contêiner for iniciado.
CMD ["python", "./client.py"]