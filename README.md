## Elastic Stack (ELK)

A configuração padrão deste projeto é propositalmente mínima. Ela não depende de nenhuma dependência externa e usa o mínimo de automação personalizada necessária para colocar os serviços em funcionamento.

Com base nas imagens oficiais do Docker da Elastic:

- Elasticsearch
- Logstash
- Kibana

Outras variantes de stack disponíveis:

- tls: criptografia TLS habilitada no Elasticsearch, Kibana (opt in) e Fleet
- searchguard: suporte ao Search Guard

## Executando a stack

Primeiramente inicialize os usuários e grupos do Elasticsearch exigidos pelo elk executando o comando:

```bash
docker compose up setup
```

Se tudo correu bem e a configuração foi concluída sem erros, inicie os outros componentes da pilha:

```bash
docker compose up -d
```

**Makefile para gerenciar comandos Docker Compose**

Este projeto fornece um `Makefile` para facilitar o gerenciamento de serviços definidos em um arquivo `docker-compose.yml`.

**Nome do arquivo Docker Compose:**

O Makefile espera que o seu arquivo de configuração do Docker Compose seja nomeado como `docker-compose.yml`. Você pode alterar essa definição na variável `DOCKER_COMPOSE_FILE` caso utilize um nome diferente.

**Comandos Disponíveis:**

Este Makefile provê diversos comandos para gerenciar os serviços do seu Docker Compose. Para utilizá-los, basta executar o comando `make` seguido do alvo desejado.

- **help:** Exibe esta mensagem de ajuda.
- **up:** Inicia todos os contêineres definidos no arquivo `docker-compose.yml` em modo detached (background).
- **down:** Para e remove todos os contêineres definidos no arquivo `docker-compose.yml`.
- **restart:** Reinicia todos os contêineres (equivalente a executar `down` seguido de `up`).
- **logs:** Exibe os logs dos contêineres em execução.
- **ps:** Mostra o status de todos os contêineres (iniciados, parados, etc.).
- **exec:** Permite executar um comando em um contêiner específico. Utilize a variável de ambiente `ARGS` para definir o nome do serviço e o comando a ser executado (exemplo: `make exec ARGS='banco-de-dados mysql -u root -p`).
- **build:** Reconstrói todas as imagens utilizadas pelos contêineres definidos no arquivo `docker-compose.yml`.
- **clean:** Remove volumes do Docker Compose que não estão sendo utilizados por nenhum contêiner.
- **remove-images** Remove todas as imagens associadas ao arquivo docker-compose.yml.

**Observação:**

- Os alvos `help`, `down`, e `clean` são marcados como `.PHONY` pois não correspondem necessariamente a arquivos reais no sistema.
- O comando `exec` utiliza a variável de ambiente `ARGS` para receber o nome do serviço e o comando a ser executado.

**Uso:**

Para utilizar um comando específico, execute o seguinte comando no terminal:

```bash
make [alvo]
```

Por exemplo, para iniciar os contêineres, execute:

```bash
make up
```

Para ver a lista de todos os alvos disponíveis, execute:

```bash
make help
```
