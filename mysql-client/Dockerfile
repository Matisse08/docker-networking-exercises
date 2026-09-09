FROM ubuntu:latest

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-client && \
    rm -rf /var/lib/apt/lists/*

