# 1. Define a imagem base
ARG VARIANT=3.12-slim-bookworm
FROM docker.io/python:${VARIANT}

# 2. Instala dependências do sistema primeiro
# Elas mudam com menos frequência, então esta camada fica no cache.
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    procps \
    && rm -rf /var/lib/apt/lists/*

# 3. Cria um usuário e grupo de sistema
# 3. Cria um usuário e grupo de sistema com um diretório home
RUN addgroup --system development && adduser --system --ingroup development --shell /bin/sh --gecos "" --home /home/dev dev

# 4. Define o diretório de trabalho
WORKDIR /home/dev/termux-assistant

# 5. Copia APENAS o arquivo de dependências e define as permissões
COPY --chown=dev:development requirements.txt ./

# 6. Instala as dependências Python. Esta camada só será reconstruída se 'requirements.txt' mudar.
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# 7. Copia o restante dos arquivos da aplicação, já com as permissões corretas
COPY --chown=dev:development . .

# 8. Define o usuário padrão para todos os comandos subsequentes
USER dev

# 9. Mantém o contêiner rodando para o VS Code
CMD [ "sleep", "infinity" ]

# 10. Metadados da imagem
LABEL org.opencontainers.image.title="Termux Assistant" \
    org.opencontainers.image.version="1.0.0"