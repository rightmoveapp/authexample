from python:3.7-slim

RUN mkdir /app
COPY . /app
RUN apt-get update -y && \
apt-get install python-pip python-dev build-essential -y  
RUN pip3 install -r /app/requirements.txt 

WORKDIR /app	
EXPOSE 8000

