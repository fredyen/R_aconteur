import urllib2
from bs4 import BeautifulSoup
import re
import csv

def urlify(s):
	# Remove all non-word characters (everything except numbers and letters)
	s = re.sub(r"[^\w\s]", ' ', s)
	# Replace all runs of whitespace with a single dash
	s = re.sub(r"\s+", '-', s)
	return s

with open('major2.csv', 'w') as csvfile:
	fieldnames = ['major', 'course', 'related']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	lines = [line.rstrip('\n') for line in open('parse_major.txt')]
	print "--------------------------------------------"


	for line in lines:

		print 'https://www.mymajors.com/college-majors/'+urlify(line)+'/'+'\n'
		page = urllib2.urlopen('https://www.mymajors.com/college-majors/'+urlify(line)+'/').read()
		soup = BeautifulSoup(page)
		soup.prettify()
		subject_str = []
		field_str = []
		for subjects in soup.findAll('ul', {"class": "cols3"}):
			for subject in subjects.findAll('li'):
				subject_str.append(subject.string)
			#print subject_str
		for fields in soup.findAll('ul', {"class": "cols2"}):
			for field in fields.findAll('li'):
				field_str.append(field.string)
			#print field_str
		
		writer.writerow({'major': line, 'course': subject_str, 'related': field_str})
		print "======="


    #writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
