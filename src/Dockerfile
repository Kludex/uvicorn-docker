ARG PYTHON_VERSION=3.10 LINUX_VERSION=
FROM python:${PYTHON_VERSION}${LINUX_VERSION:+-$LINUX_VERSION}

LABEL maintainer="Marcelo Trylesinski <marcelotryle@gmail.com>"

ENV UVICORN_HOST 0.0.0.0
ENV UVICORN_PORT 8000
ENV UVICORN_LIFESPAN on

COPY requirements.txt /tmp/requirements.txt
RUN /usr/local/bin/python -m pip install --no-cache-dir -r /tmp/requirements.txt \
    && mkdir /docker-entrypoint.d

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

WORKDIR /app

COPY main.py /app/main.py

EXPOSE 8000

CMD ["uvicorn", "main:app"]
