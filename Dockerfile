FROM python:alpine3.21

WORKDIR /app

COPY requirements.txt config.json ./

RUN pip install --no-cache-dir -r requirements.txt

COPY /modules ./modules/
COPY assistant.py .

ENTRYPOINT [ "python", "assistant.py" ]

CMD [ "--dashboard" ]

LABEL org.opencontainers.image.title="Termux Assistant" \
    org.opencontainers.image.version="1.0.0"