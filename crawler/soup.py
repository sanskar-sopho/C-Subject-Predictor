from bs4 import BeautifulSoup
import urllib2


def extract_code(url,file_name):
	page=urllib2.urlopen(url)
	soup=BeautifulSoup(page,'xml')
	file=open(file_name,'w')
	
	# repcontent=(soup.find(class_="repository-content")).find_all('table')
	# for row in soup.find(class_="repository-content").find_all("tr"):
	# 	print(row,'\n')
	tables=soup.findChildren('table')
	# print(tables)
	my_table=tables[0]
	rows=my_table.findChildren(['th','tr'])
	line=0
	for row in rows:
		print(line)
		line+=1
		for string in row.stripped_strings:
			string=str(unicode(string))
			print(string)
			file.write(string)
			file.write(' ')
			# spans=cells[1].findChildren('span')
			# for span in spans:
				# print(span.string)
		file.write('\n')


url="https://github.com/kimiyoung/ssl_bad_gan/blob/master/cifar_trainer.py"
file_name='code.txt'
extract_code(url,file_name)