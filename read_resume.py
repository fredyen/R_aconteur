import json
from pprint import pprint
import re

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


def edu_str():
    with open('resumes-1.json') as data_file:    
        data = json.load(data_file)[1]

        ndata = data["resume_content"]
        #education
        edulist = ['Education:','EDUCATION']
        for xd in edulist:
            if xd in ndata:
                edufrt = ndata.find(xd)
                break
            else:
                edufrt = -1

        if (edufrt != -1):
            #pprint(edufrt) 
            eduend = ndata[edufrt+9:]
            edunxt = find_nth(eduend,':',2)

            edunxt = eduend[:edunxt]
            education = re.sub('\W+',' ', edunxt)

        else:
            education = "None"

    return education

def exp_str():
    with open('resumes-1.json') as data_file:    
        data = json.load(data_file)[1]

        ndata = data["resume_content"]
    
        #experience
        explist = ['Experience:','Experience','PROFESSIONAL EXPERIENCE']
        for x in explist:
            if x in ndata:
                expfrt = ndata.find(x)
                #print expfrt
                break
            else:
                expfrt = -1
        #frt = ndata.find('Experience:')
        if expfrt != -1:
            expend = ndata[expfrt:]
            nxt = find_nth(expend,':',2)

            expnxt = expend[:nxt]
            experience = re.sub('\W+',' ', expnxt)
        else:
            #print "here"
            experience = "None"
    
    return experience






