FROM docker.io/python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt config.json ./

RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

COPY /modules modules/
COPY assistant.py .

RUN groupadd -r appgroup && useradd -r -g appgroup appuser && chown -R appuser:appgroup /app
USER appuser

ENTRYPOINT [ "python", "assistant.py" ]

CMD [ "--dashboard" ]

LABEL org.opencontainers.image.title="Termux Assistant" \
    org.opencontainers.image.version="1.0.0"