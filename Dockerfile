# FROM rust:slim-buster
FROM python:slim-buster

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
        build-essential 
        
# Clean up
RUN apt-get autoremove -y &&\
    apt clean

# Get python libs
#TODO: Check for more libraries
# RUN python3 python3-pip &&\
#     pip3 install rpi.gpio &&\
RUN pip install sphinx &&\
    pip install sphinx_rtd_theme\
    pip install black


WORKDIR /home/src