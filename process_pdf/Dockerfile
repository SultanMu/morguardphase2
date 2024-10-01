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
CMD ["uvicorn", "pdf_processor:app", "--host", "0.0.0.0", "--port", "8000","--loop", "asyncio", "--workers", "4", "--limit-max-requests", "10"]
