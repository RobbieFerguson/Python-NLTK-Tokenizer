# #FROM python:2-onbuild

# FROM python:2.7

# #RUN sudo apt-get update
# #RUN sudo apt-get install -y python

# COPY . /src

# RUN cd /src; pip install --no-cache-dir -r requirements.txt;


# CMD ["python", "/src/app.py"]

FROM python:2.7

RUN pip install -U nltk

COPY . / src

RUN cd /src; pip install --no-cache-dir -r requirements.txt;

ENV CORPORA brown
CMD python -m nltk.downloader $CORPORA; python

CMD ["python", "/src/app.py"]