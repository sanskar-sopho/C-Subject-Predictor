import numpy as np
import tensorflow as tf
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","1698809","Comments" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = 'Select COMMENT_TEXT from AllComments';
cursor.execute(sql)
AllWords = []
for row in cursor:
    comment = row[0];
    words = comment.split()
    # print(words)
    for w in words :	
        AllWords.append(w)

Unique_Words = list(set(AllWords))
# print(Unique_Words)
db.close()

word2int={}
int2word={}
for i,word in enumerate(Unique_Words):
	word2int[word]=i
	int2word[i]=word


