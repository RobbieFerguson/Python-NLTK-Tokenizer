import os
import re
import nltk
import json
from pprint import pprint

nltk.download('punkt')
nltk.download('maxent_treebank_pos_tagger')

from nltk.tokenize import word_tokenize, wordpunct_tokenize

# print "CWD"
# print os.getcwd()

with open('./ahab/output.json') as data:
	d = json.load(data)

toReturn = {}

for movie in d["MovieReviews"]:
	review = movie["Review"] 
	review = re.sub("<[^>]*>", "",movie["Review"])
	rating = movie["Rating"]


	tokens = word_tokenize(review)
	tagged = nltk.pos_tag(tokens)

	if rating in toReturn:
		toReturn[rating] += tagged
	else:
		toReturn[rating] = tagged





with open('./ahab/output.json', 'w+') as outfile:
	json.dump(toReturn, outfile)
	print "SUCCESSFULLY OUTPUT TO JSON IN PYTHON"


print "WORKING IN PYTHON"

