FROM python:3.9-alpine
WORKDIR /app
USER root
RUN apk update && \
    apk add \
    build-base \
    libffi-dev \
    openssl-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
ENV GUNICORN_CMD_ARGS="--worker-class uvicorn.workers.UvicornWorker --workers=4 --bind 0.0.0.0:8000 --timeout 240 --log-level debug --access-logfile - --error-logfile -" 
CMD ["gunicorn", "morguard.asgi:application"]
# CMD ["python3","manage.py","runserver"]