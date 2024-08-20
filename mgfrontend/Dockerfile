FROM node:20.5-alpine3.17
USER root
WORKDIR /app
RUN apk update && \
    apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev
RUN apk update && \
    apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev
COPY package.json ./
RUN npm install -g @angular/cli
RUN npm install --force
COPY . .
EXPOSE 4201
CMD ["ng", "serve","--host", "0.0.0.0","--port","4201", "--disable-host-check"]
