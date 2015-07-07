FROM ubuntu:latest

# Install required packages
RUN apt-get update
RUN apt-get -y install python

ADD . /app

RUN cd /app; pip install -r requirements.txt

# Set the default command to run
CMD ["python", "app.py"]