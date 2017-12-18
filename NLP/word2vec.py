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
sentences = []
for row in cursor:
    comment = row[0];
    sentences.append(comment)
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

# print(sentences[78])
train_data=[]
WINDOW_SIZE=1
for sentence in sentences:
	words=sentence.split()
	for index in range(0,len(words)):
		for i in range(-1*WINDOW_SIZE,WINDOW_SIZE+1,1):
			if(index+i<0 or i==0 or index+i>=len(words)):
				continue
			train_data.append([words[index],words[index+i]])
	
# print train_data
# print(len(train_data))
# print(sentences[len(sentences)-3])

