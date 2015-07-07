import os
import re
import nltk
import requests
import json
# from ahab import output.json


from nltk.corpus import stopwords

# print stopwords.words("english")

# letters_only = re.sub("[^a-zA-Z]", " ", input.json)

# print letters_only

# r = requests.get('http://www.myapifilms.com/imdb/comingSoon')

# with open('../ahab_demo1_node/output.json', 'wb') as f:
# 	for chunk in r.iter_content(chunk_size=1024):
# 		if chunk:
# 			f.write(chunk)

data = []
with open('output.json') as f:
	for line in f:
		data.append(json.loads(line))

print "PRINTING FROM PYTHON"
print data
