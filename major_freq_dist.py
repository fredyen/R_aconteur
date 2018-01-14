import nltk
from nltk.probability import FreqDist
from collections import Counter
import glob, os
import math
from read_resume import edu_str, exp_str
import re
import csv
import pygal
import numpy

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)

def second_largest(numbers):
    first, second = None, None
    for n in numbers:
        if n > first:
            first, second = n, first
        elif first > n > second:
            second = n
    return second

# Get education list
edu_str = edu_str()
edu_str = edu_str.replace('[^0-9a-zA-Z]+', ' ')
edu_str = edu_str.replace(',', ' ')
edu_str = edu_str.replace('/', ' ')
edu_str = edu_str.replace('(', ' ')
edu_str = edu_str.replace(')', ' ')
edu_str = edu_str.replace('and', ' ')

tokens = nltk.word_tokenize(edu_str)
fdist = FreqDist(tokens)
counterA_edu = Counter(fdist)#.most_common(20)

MAX_major = " "
MAX_sim_edu = 0
SEC_major = " "
SEC_sim_edu = 0
major_sim_list = []
major_list = []
counterB_maj_list = []

# Get exp list
exp_str = exp_str()
exp_str = exp_str.replace('[^0-9a-zA-Z]+', ' ')
exp_str = exp_str.replace(',', ' ')
exp_str = exp_str.replace('/', ' ')
exp_str = exp_str.replace('(', ' ')
exp_str = exp_str.replace(')', ' ')
exp_str = exp_str.replace('and', ' ')

tokens_exp = nltk.word_tokenize(exp_str)
fdist_exp = FreqDist(tokens_exp)
counterA_exp = Counter(fdist_exp)

MAX_industry = " "
MAX_sim_ind = 0
SEC_industry = " "
SEC_sim_ind = 0
Industry_sim_list = []
Industry_list = []
counterB_ind_list = []

# Compare Education distributions
print "-------------------"
print"Start comparing Major/Education distributions:"
for filename in sorted(glob.glob('./majors/*.txt')):
	# Load all majors fdist
	with open(filename, "r")  as filename_list:
		filename_str = filename_list.read().replace('[^0-9a-zA-Z]+', ' ')
		filename_str = filename_str.replace(',', ' ')
		filename_str = filename_str.replace('/', ' ')
		filename_str = filename_str.replace('(', ' ')
		filename_str = filename_str.replace(')', ' ')
		filename_str = filename_str.replace('and', ' ')
	tokens_filename = nltk.word_tokenize(filename_str)
	fdist_filename = FreqDist(tokens_filename)
	counterB_maj = Counter(fdist_filename)
	sim_edu = counter_cosine_similarity(counterA_edu, counterB_maj)
	major_sim_list.append(sim_edu)
	major_list.append(filename[9:])
	counterB_maj_list.append(counterB_maj)

MAX_sim_maj = max(major_sim_list)
SEC_sim_maj = second_largest(major_sim_list)
MAX_major = major_list[major_sim_list.index(MAX_sim_maj)]
SEC_major = major_list[major_sim_list.index(SEC_sim_maj)]
#if sim_edu > MAX_sim_edu:
#	MAX_sim_edu = sim_edu
#	MAX_major = filename
norm_maj_sim_list = [x / MAX_sim_maj for x in major_sim_list]
print "-------------------"
print "Normalized sim = ", norm_maj_sim_list
print "Max sim_maj = ", MAX_sim_maj
print "Max major = ", MAX_major
print "Second sim_maj = ", SEC_sim_maj
print "Second major = ", SEC_major
between_maj = counter_cosine_similarity(counterB_maj_list[major_sim_list.index(MAX_sim_maj)], counterB_maj_list[major_sim_list.index(SEC_sim_maj)])
print "Sim of two majors = ", between_maj

# Compare Experience distributions
print "-------------------"
print"Start comparing Industry/Experience distributions:"
for csvfile in sorted(glob.glob('./industries/*.csv')):
	with open(csvfile, 'rb') as csv_list:
		file_reader = csv.reader(csv_list)
		file_list = list(file_reader)

	ind_str = ''.join(str(voc) for voc in file_list).replace('[^0-9a-zA-Z]+','')
	ind_str = ind_str.replace(']',' ')
	ind_str = ind_str.replace("'",' ')
	ind_str = ind_str.replace('[',' ')
	ind_str = ind_str.replace(',',' ')
	ind_str = ind_str.replace('and',' ')

	tokens_ind = nltk.word_tokenize(ind_str)
	fdist_ind = FreqDist(tokens_ind)
	counterB_ind = Counter(fdist_ind)
	sim_ind = counter_cosine_similarity(counterA_exp, counterB_ind)
	Industry_sim_list.append(sim_ind)
	Industry_list.append(csvfile[13:])
	counterB_ind_list.append(counterB_ind)
#print Industry_sim_list
#if sim_ind > MAX_sim_ind:
#	MAX_sim_ind = sim_ind
#	MAX_industry = csvfile
MAX_sim_ind = max(Industry_sim_list)
SEC_sim_ind = second_largest(Industry_sim_list)
MAX_industry = Industry_list[Industry_sim_list.index(MAX_sim_ind)]
SEC_industry = Industry_list[Industry_sim_list.index(SEC_sim_ind)]
norm_ind_sim_list = [x / MAX_sim_ind for x in Industry_sim_list]
print "-------------------"
print "Normalized sim = ", norm_ind_sim_list
print "Max sim_ind = ", MAX_sim_ind
print "Max industry = ", MAX_industry
print "Second sim_ind = ", SEC_sim_ind
print "Second industry = ", SEC_industry
between_ind = counter_cosine_similarity(counterB_ind_list[Industry_sim_list.index(MAX_sim_ind)], counterB_ind_list[Industry_sim_list.index(SEC_sim_ind)])
print "Sim of two industries = ", between_ind

#-----------------------------------------------------------------
# DATA VISUALIZATION
maj_std = numpy.std(major_sim_list, axis=0)
maj_mean = numpy.mean(major_sim_list, axis=0)
ind_std = numpy.std(Industry_sim_list, axis=0)
ind_mean = numpy.mean(Industry_sim_list, axis=0)

radar_chart = pygal.Radar(fill=True)
radar_chart.title = 'R_aconteur Advanced Analysis'
radar_chart.x_labels = ["Major Difference", 'Between Major Domain', "Industry Difference", 'Between Industry Domain']
radar_chart.add('Candidate', [(MAX_sim_maj-SEC_sim_maj)/MAX_sim_maj, between_maj, (MAX_sim_ind-SEC_sim_ind)/MAX_sim_ind, between_ind])
radar_chart.render_to_file('radar.svg')

Z1 = [x for _,x in sorted(zip(norm_maj_sim_list, major_list),reverse=True)]
Z2 = [x for x,_ in sorted(zip(norm_maj_sim_list, major_list),reverse=True)]
# Dot - Major
majtop = []

dot_chart = pygal.Dot(x_label_rotation=30)
dot_chart.title = 'Major Categorical'
dot_chart.x_labels = Z1[:5]
dot_chart.add('Candidate', Z2[:5])

dot_chart.render_to_file('majtop.svg')

# Dot - Industry
Z3 = [x for _,x in sorted(zip(norm_ind_sim_list, Industry_list),reverse=True)]
Z4 = [x for x,_ in sorted(zip(norm_ind_sim_list, Industry_list),reverse=True)]
indtop = [] 

dot_chart = pygal.Dot(x_label_rotation=30)
dot_chart.title = 'Industry Categorical'
dot_chart.x_labels = Z3[:5]
dot_chart.add('Candidate', Z4[:5])

dot_chart.render_to_file('indtop.svg')




