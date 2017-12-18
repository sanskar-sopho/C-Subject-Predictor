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
    print(words)
    for w in words :	
        AllWords.append(w)
# print('-----------List of All the Words----------------')
# print(FinalStrWords)
# print('------------Count of All words------------------')
# print(len(FinalStrWords))

Unique_Words = list(set(AllWords))
# print('------------List of Unique Words----------------')
print(Unique_Words)
# print('------------Count of Unique Words---------------')
# print(len(Unique_Word_List))
db.close()
