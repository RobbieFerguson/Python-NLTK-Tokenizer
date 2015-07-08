#FROM python:2-onbuild

FROM python:2.7

#RUN sudo apt-get update
#RUN sudo apt-get install -y python

COPY . /src

RUN cd /src; pip install --no-cache-dir -r requirements.txt; python -c 'import nltk ; nltk.download()''


#CMD ["python", "import nltk",";", "nltk.download()"]
CMD ["python", "/src/app.py"]