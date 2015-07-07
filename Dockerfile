FROM ubuntu:latest

# Install required packages
RUN apt-get update
RUN apt-get -y install python

# Add python app code to the image
RUN mkdir -p /app
ADD. /app
WORKDIR /app

RUN pip install requirements.txt

# Set the default command to run
CMD ["python", "app.py"]