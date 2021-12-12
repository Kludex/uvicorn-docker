FROM uvicorn:latest

RUN pip install --no-cache-dir fastapi==0.70.1

COPY main.py /app/
COPY script.sh /docker-entrypoint.d/
