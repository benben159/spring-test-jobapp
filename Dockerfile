FROM maven:3.6-openjdk-11-slim as builder
WORKDIR /root/app
COPY . /root/app
RUN mvn package -Dmaven.test.skip

FROM openjdk:11-jre-slim
ARG JAR_FILE=/root/app/target/*.jar
COPY --from=builder ${JAR_FILE} app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]

