import MySQLdb
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
from nltk import pos_tag, word_tokenize



stemmer = PorterStemmer()
# Open database connection
db = MySQLdb.connect("localhost","root","root","Comments" )

# prepare a cursor object using cursor() method
cursor = db.cursor()


db1 = MySQLdb.connect("localhost","root","root","Comments" )

# prepare a cursor object using cursor() method
cursor1 = db1.cursor()


'''
Fields of AllComments
id , FILE_NAME,START_LINE, END_LINE, COMMENT_TEXT
'''

'''
CommentAnalysis (
           id INT NOT NULL AUTO_INCREMENT primary key,
           CommentId INT,
	   KeywordNo INT,
           Keyword VARCHAR(100) NOT NULL,
           VocabType VARCHAR(100),
           POSTYPE VARCHAR(50),
           StemmedWord VARCHAR(100),
           StemmedVocabType VARCHAR(100),
           StemmedPOSTYPE VARCHAR(100),
           FOREIGN KEY (CommentId)
           REFERENCES AllComments(id)
           ON DELETE CASCADE
         )



'''


import csv

'''
Algorithm	Performance	Access Scope	Memory	State	Streams	Concurrency	Operation	Data Structure (storage)	Domain	Security	Problem	Class	Unit	Number	Nouns	Conjunction	Verbs


'''



f = csv.reader(open('VocabsCsv.csv'))
Algorithm, Performance, Access_Scope, Memory, State , Streams, Concurrency, Operation, Data_Structure, Domain, Security, Problem, Class, Unit, Number, Nouns, Conjunction , Verbs = zip(*f)


def InsertStemmedWord(CId, KeywordNo ,word, stemmedWord , VocabType) :
        #print "Insert Called " + str(CId) + " " + str(KeywordNo) + " " +str(word) + " " + str(VocabType)
	sql = "INSERT INTO CommentAnalysis ( CommentId, KeywordNo , Keyword, StemmedWord, StemmedVocabType) VALUES (" + str(CId) + ", " + str(KeywordNo) + " , '" + word +  "' , '" + stemmedWord + "','" + VocabType + "')";
	print sql 
	try:
       # Execute the SQL command
   		cursor1.execute(sql)
   # Commit your changes in the database
   		db1.commit()
		
	except:
 		print "Error in insertion"
   # Rollback in case there is any error
   		#db1.rollback()





def Insert(CId, KeywordNo , word , VocabType) :
        #print "Insert Called " + str(CId) + " " + str(KeywordNo) + " " +str(word) + " " + str(VocabType)
	sql = "INSERT INTO CommentAnalysis ( CommentId, KeywordNo , Keyword, VocabType) VALUES (" + str(CId) + ", " + str(KeywordNo) + " , '" + word + "','" + VocabType + "')";
	print sql 
	try:
       # Execute the SQL command
   		cursor1.execute(sql)
   # Commit your changes in the database
   		db1.commit()
		
	except:
 		print "Error in insertion"
   # Rollback in case there is any error
   		#db1.rollback()


def InsertIntoDB(CId , Words) :
	print "called"
	
	KeywordNo = 1
	for word in Words :
	    print(word)
	    stemmedWord = ''
	    try:
                print('Trying to stem - ' + word)
		stemmedWord = stemmer.stem(word)
                print('************** ' + word + ' ' + stemmedWord)
	    except:
		   print('Cannot stem')

            if word in Operation :
		print '*******************************************Found in operation'
	    if stemmedWord in Operation :
		print '*******************************************Found in operation'


	    if word in Algorithm :
		Insert(CId ,KeywordNo, word, 'Algorithm')
	    elif stemmedWord in Algorithm :
		InsertStemmedWord(CId , KeywordNo , word,stemmedWord , 'Algorithm')

  	    if word in Performance :
		Insert(CId, KeywordNo, word , 'Performance')
	    elif stemmedWord in Performance :
		InsertStemmedWord(CId , KeywordNo , word, stemmedWord , 'Performance')


	    if word in 	Access_Scope :
		Insert(CId , KeywordNo, word , 'Access_Scope')
	    elif stemmedWord in Access_Scope :
		InsertStemmedWord(CId , KeywordNo ,word, stemmedWord , 'Access_Scope')
	

	    if word in Memory :
		Insert(CId , KeywordNo, word , 'Memory')
	    elif stemmedWord in Memory :
		InsertStemmedWord(CId , KeywordNo ,word, stemmedWord , 'Memory')


	    if word in State :
		Insert(CId , KeywordNo, word , 'State')
	    elif stemmedWord in State :
		InsertStemmedWord(CId , KeywordNo ,word, stemmedWord , 'State')
	    
            if word in Streams :
		Insert(CId , KeywordNo, word , 'Streams')
	    elif stemmedWord in Streams :
		InsertStemmedWord(CId , KeywordNo ,word, stemmedWord , 'Streams')
	    
	    if word in Concurrency :
		Insert(CId , KeywordNo, word , 'Concurrency')
	    elif stemmedWord in Concurrency :
		InsertStemmedWord(CId , KeywordNo ,word, stemmedWord , 'Concurrency')

	    if word in Operation :
		Insert(CId , KeywordNo, word , 'Operation')
	    elif stemmedWord in Operation :
		InsertStemmedWord(CId , KeywordNo ,word, stemmedWord , 'Operation')

	    if word in Data_Structure :
		Insert(CId , KeywordNo, word , 'Data_Structure')
	    elif stemmedWord in Data_Structure :
		InsertStemmedWord(CId , KeywordNo , word,stemmedWord , 'Data_Structure')

	    if word in Domain :
		Insert(CId , KeywordNo, word , 'Domain')
	    elif stemmedWord in Algorithm :
		InsertStemmedWord(CId , KeywordNo , word,stemmedWord , 'Domain')

    	    if word in Security :
		Insert(CId , KeywordNo, word , 'Security')
	    elif stemmedWord in Security :
		InsertStemmedWord(CId , KeywordNo ,word, stemmedWord , 'Security')

	    if word in Problem :
		Insert(CId , KeywordNo, word , 'Problem')
	    elif stemmedWord in Problem :
		InsertStemmedWord(CId , KeywordNo , word,stemmedWord , 'Problem')

	    if word in 	Class :
		Insert(CId , KeywordNo, word , 'Class')
	    elif stemmedWord in Class :
		InsertStemmedWord(CId , KeywordNo , word,stemmedWord , 'Class')

	    if word in 	Unit :
		Insert(CId , KeywordNo, word , 'Unit')
	    elif stemmedWord in Unit :
		InsertStemmedWord(CId , KeywordNo ,word, stemmedWord , 'Unit')

	    if word in 	Number :
		Insert(CId , KeywordNo, word , 'Number')
	    elif stemmedWord in Number :
		InsertStemmedWord(CId , KeywordNo ,word, stemmedWord , 'Number')

	    if word in Nouns :
		Insert(CId , KeywordNo, word , 'Nouns')
	    elif stemmedWord in Algorithm :
		InsertStemmedWord(CId , KeywordNo , word,stemmedWord , 'Nouns')


 	    if word in Conjunction :
		Insert(CId , KeywordNo, word , 'Conjunction')
	    elif stemmedWord in Conjunction :
		InsertStemmedWord(CId , KeywordNo , word,stemmedWord , 'Conjunction')

	    if word in Verbs :
		Insert(CId , KeywordNo, word , 'Verbs')
	    elif stemmedWord in Verbs :
		InsertStemmedWord(CId , KeywordNo , word,stemmedWord , 'Verbs')

 	    KeywordNo = KeywordNo + 1




def InsertPosTag(CId , KeywordNo , word , POSTag):
	sql = "INSERT INTO CommentAnalysis ( CommentId, KeywordNo , Keyword, POSTYPE) VALUES (" + str(CId) + ", " + str(KeywordNo) + " , '" + word + "','" + POSTag + "')";
	print sql 
	try:
       # Execute the SQL command
   		cursor1.execute(sql)
   # Commit your changes in the database
   		db1.commit()
		
	except:
 		print "Error in insertion for POS"
   # Rollback in case there is any error
   		#db1.rollback()





def POSTagging(CId , commentText) :
    text = word_tokenize(commentText)
    t = nltk.pos_tag(text)
    i = 1
    for pair in t:
	print(pair[0])
	print(pair[1])
	InsertPosTag(CId , i , pair[0] , pair[1])
	i = i + 1




sql = "SELECT id , FILE_NAME,START_LINE, END_LINE, COMMENT_TEXT FROM AllComments"




try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      CId = row[0]
      CText = row[4]
      POSTagging(CId , CText)	
      #print "Comment --- " + CText
      Words = word_tokenize(CText)
      InsertIntoDB(CId , Words)
      # Now print fetched result
      #print "CId=%d,CText=%s" % (CId, CText)
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
