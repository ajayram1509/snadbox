FROM ubuntu:18.04

RUN apt-get update -y
RUN apt install -y build-essential
RUN apt-get install -y manpages-dev
RUN apt-get install -y python3
RUN apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/ && \
    rm -rf /var/cache/oracle-jdk8-installer;
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME
RUN apt-get install -y ca-certificates
RUN apt-get update -y && apt-get install -y curl
ARG NODE_VERSION=16.14.2
ARG NODE_PACKAGE=node-v$NODE_VERSION-linux-x64
ARG NODE_HOME=/opt/$NODE_PACKAGE

ENV NODE_PATH $NODE_HOME/lib/node_modules
ENV PATH $NODE_HOME/bin:$PATH

RUN curl https://nodejs.org/dist/v$NODE_VERSION/$NODE_PACKAGE.tar.gz | tar -xzC /opt/

# comes with npm
RUN npm install -g typescript
RUN apt install -y git
RUN git clone https://github.com/ioi/isolate.git
RUN apt-get install -y libcap-dev
RUN cd isolate && chmod 777 .
RUN cd isolate && make install && cd
RUN isolate --init
#RUN pip3 install flask
RUN mkdir app
COPY . app
WORKDIR  app