#FROM python:2-onbuild

# Set the default command to run
#CMD ["python", "./app.py"]


FROM ubuntu:14.04

RUN sudo apt-get update
RUN sudo apt-get install -y python

COPY . /src

RUN cd /src
RUN pip install -r requirments.txt

CMD ["python", "/src/app.py"]