import nltk
import csv
from nltk.probability import FreqDist
from collections import Counter
import re
import csv
import glob

for csvfile in sorted(glob.glob('./industries/*.csv')):
	with open(csvfile, 'rb') as csv_list:
		file_reader = csv.reader(csv_list)
		file_list = list(file_reader)


	str11 = ''.join(str(voc) for voc in file_list).replace('[^0-9a-zA-Z]+','')

	str11 = str11.replace(']',' ')
	str11 = str11.replace("'",' ')
	str11 = str11.replace('[',' ')
	str11 = str11.replace(',',' ')
	str11 = str11.replace('and',' ')

	tokens = nltk.word_tokenize(str11)
	fdist11 = FreqDist(tokens)

	top = Counter(fdist11).most_common(50)


