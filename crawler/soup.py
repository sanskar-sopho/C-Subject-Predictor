from bs4 import BeautifulSoup
import urllib2
import sys
import os

repo="https://github.com/kennyledet/Algorithm-Implementations"
base_link='https://github.com'

def get_file_count():
	files=os.listdir('codes/')
	return len(files)

file_count=get_file_count()

def extract_code(url,file_name):
	print 'file : ',url
	global file_count
	# if(file_count>=50):
	# 	sys.exit
	page=urllib2.urlopen(url)
	soup=BeautifulSoup(page,'xml')
	file=open('codes/'+file_name,'w')
	file_count+=1
	# repcontent=(soup.find(class_="repository-content")).find_all('table')
	# for row in soup.find(class_="repository-content").find_all("tr"):
	# 	print(row,'\n')
	# date=soup.find_all(datetime=True)
	try:
		urllib2.urlopen(url)
		date=soup.findChildren(['relative-time'])
		# print("Date is ",date)
		if(date!=[]):
			datetime=date[0]['datetime']
			# print "Date : ",datetime
		else:
			datetime='Date Not Available'
		tables=soup.findChildren('table')
		# print(tables)
		my_table=tables[0]
		rows=my_table.findChildren(['th','tr'])
		
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
		label_file.write('codes/'+str(file_count-1)+'.txt '+url+'\n')
		file.close()
		return datetime
	except:
		print("Error in this file")
		file_count-=1
		return -1

def expand_folder(url):
	global file_count
	print "folder : ", url
	page=urllib2.urlopen(url)
	soup=BeautifulSoup(page,'xml')
	table=soup.find('table')
	rows=table.find_all(['th','tr'])
	for row in rows:
		if(('js-navigation-item' not in row['class']) or ('up-tree' in row['class'])):
			continue
		cols=row.find_all('td')
		for col in cols:
			if('content' not in col['class']):
				continue
			tag=col.find('a')
			link=tag['href']
			if('README' in link):
				continue
			if('tree/master' in link):
				expand_folder(base_link+link)
			# print type(link)
			if(('blob/master' in link) and ('.c' in link) and ('.csv' not in link)):
				datetime=extract_code(base_link+link,str(file_count)+'.txt')
				if(datetime != -1):
					print 'file written , Date : ', datetime
			else:
				continue

label_file=open('labels.txt','a')
expand_folder(repo)
label_file.close()