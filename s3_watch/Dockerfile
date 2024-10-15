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
CMD ["python", "s3_watch.py","-i","10"]
