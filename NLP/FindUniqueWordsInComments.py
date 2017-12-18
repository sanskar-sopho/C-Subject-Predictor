import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","Comments" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = 'Select COMMENT_TEXT from AllComments';
cursor.execute(sql)
FinalStrWords = []
for row in cursor:
    comment = row[0];
    words = comment.split()
    print(words)
    for w in words :	
        FinalStrWords.append(w)
print('-----------List of All the Words----------------')
print(FinalStrWords)
print('------------Count of All words------------------')
print(len(FinalStrWords))

Unique_Word_List = list(set(FinalStrWords))
print('------------List of Unique Words----------------')
print(Unique_Word_List)
print('------------Count of Unique Words---------------')
print(len(Unique_Word_List))
db.close()
