FROM ubuntu:latest

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt-get install -y \
    python3.9 \
    python3-pip \
    make
RUN alias python3=/usr/bin/python3.9
COPY ./ /app/library/
RUN ls /app/library
RUN cd /app/library && make setup
RUN cd /app/library && make update
RUN cd /app/library && make startdev


CMD ["bash"]