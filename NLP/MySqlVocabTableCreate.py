import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","Comments" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS CommentAnalysis")

sql = """ CREATE TABLE CommentAnalysis (
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
         )"""
cursor.execute(sql)


db.close()
