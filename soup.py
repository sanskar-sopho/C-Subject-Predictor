from bs4 import BeautifulSoup
import urllib2

url="http://www.cprogramming.com/snippets/source-code/templated-stack-class"
page=urllib2.urlopen(url)

soup=BeautifulSoup(page,'html.parser')
table=soup.find_all('table',class_='main')
for 