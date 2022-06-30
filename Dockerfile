FROM maven:3.6-openjdk-11-slim as builder
WORKDIR /root/app
COPY . /root/app
RUN mvn package
