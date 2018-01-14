from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_doc, 'html.parser')
with open("https___www.mymajors.com_college_majors_.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#print(soup.prettify())
#soup.find_all('expanded top')

lis = soup.find_all("li", {"class": "leaf"})

print "------------------------------------"

text_file = open("parse_major.txt", "w")

for li in lis:
	if li.a is None:
		print "Is None"
	else:
		print li.a.string
		text_file.write(li.a.string)
		text_file.write("\n")

text_file.close()
