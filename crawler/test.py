from bs4 import BeautifulSoup
import urllib2
import sys

repo="https://github.com/sanskar-sopho/models/blob/master/official/mnist/__init__.py"
base_link='https://github.com'
file_count=0

def extract_code(url,file_name):
	print 'file : ',url
	global file_count
	if(file_count>=50):
		sys.exit
	page=urllib2.urlopen(url)
	soup=BeautifulSoup(page,'xml')
	file=open(file_name,'w')
	file_count+=1
	# repcontent=(soup.find(class_="repository-content")).find_all('table')
	# for row in soup.find(class_="repository-content").find_all("tr"):
	# 	print(row,'\n')
	# date=soup.find_all(datetime=True)
	date=soup.findChildren(['relative-time'])
	print date
	datetime=date[0]['datetime']
	tables=soup.findChildren('table')
	# print(tables)
	print tables
	my_table=tables[0]
	rows=my_table.findChildren(['th','tr'])
	print rows
	if(rows==[]):
		print "fe"
	line=0
	for row in rows:
		# print(line)
		line+=1
		for string in row.stripped_strings:
			string=str(unicode(string))
			# print(string)
			file.write(string)
			file.write(' ')
			# spans=cells[1].findChildren('span')
			# for span in spans:
				# print(span.string)
		file.write('\n')
	return datetime


datetime=extract_code(repo,'test.txt')
print datetime