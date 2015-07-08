import os
import re
import nltk
import requests
import json
from pprint import pprint
# from ahab import output.json


from nltk.corpus import stopwords

# print stopwords.words("english")

# letters_only = re.sub("[^a-zA-Z]", " ", input.json)

# print letters_only

# r = requests.get('http://www.myapifilms.com/imdb/comingSoon')

print "CWD"
print os.getcwd()

with open('../ahab/output.json') as data:
	d = json.load(data)
	pprint(d)

print "DONE PRINTING IN PYTHON"

with open('..containers/ahab/python_output.json', 'w') as outfile:
	json.dump(d, outfile)
	print "SUCCESSFULLY OUTPUT TO JSON"