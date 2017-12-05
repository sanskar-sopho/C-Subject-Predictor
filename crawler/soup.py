from bs4 import BeautifulSoup
import urllib2

url="https://github.com/sanskar-sopho/Cat-Dog_classifier/blob/master/cat_dog.py"
page=urllib2.urlopen(url)

soup=BeautifulSoup(page,'html.parser')	
# repcontent=(soup.find(class_="repository-content")).find_all('table')
# for row in soup.find(class_="repository-content").find_all("tr"):
# 	print(row,'\n')

tables=soup.findChildren('table')
# print(tables)
my_table=tables[0]
rows=my_table.findChildren(['th','tr'])
for row in rows:
	cells=row.findChildren('td')
	span=cells[1].findChildren('span')
	print(span)