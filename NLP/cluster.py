import numpy as np
import tensorflow as tf
import MySQLdb
import math
from tensorflow.contrib.layers import fully_connected

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

train_x=[]
train_y=[]
for data in train_data:
	train_x.append(word2int[data[0]])
	train_y.append(word2int[data[1]])
train_x=np.array(train_x)
train_y=np.array(train_y)
train_x=np.reshape(train_x,[-1,1])
train_y=np.reshape(train_y,[-1,1])
print(train_x.shape,train_y.shape)

vocab_size=len(Unique_Words)
embed_size=100
num_sampled=30
num_iter=10000

X=tf.placeholder(tf.int32,shape=[None,1])
Y=tf.placeholder(tf.int32,shape=[None,1])

embeddings=tf.Variable(tf.random_uniform([vocab_size,embed_size],-1.0,1.0),dtype=tf.float32)
soft_weights=tf.Variable(tf.truncated_normal([vocab_size,embed_size],stddev=1.0/math.sqrt(embed_size)),dtype=tf.float32)
soft_biases=tf.Variable(tf.zeros([vocab_size]),dtype=tf.float32)
# print soft_weights,soft_biases

# temp=tf.Variable(tf.zeros([None,embed_size]))
embed=tf.nn.embedding_lookup(embeddings,X)
embed=tf.reduce_sum(embed,1)
print embed
print Y
loss=tf.reduce_mean(tf.nn.sampled_softmax_loss(soft_weights,soft_biases,Y,embed,num_sampled,vocab_size))

optimizer=tf.train.AdagradOptimizer(0.1).minimize(loss)

def train():
	saver=tf.train.Saver([embeddings,soft_weights,soft_biases])
	for i in range(0,num_iter):
		feed_dict={X:train_x,Y:train_y}
		_,l=sess.run([optimizer,loss],feed_dict)
		if(i%100==0):
			print i," loss = ",l
		if(i%10000==0 and i != 0):
			save_path=saver.save(sess,'restore/len_26/model.ckpt')
			print "Successfully saved in ",save_path	
	save_path=saver.save(sess,'restore/len_26/model.ckpt')
	print "Successfully saved in ",save_path

def restore():
	saver=tf.train.Saver([embeddings,soft_weights,soft_biases])
	# tf.reset_default_graph()
	saver.restore(sess,"restore/len_100/model.ckpt")
	print "Successfully Restored"


with tf.Session() as sess:
	tf.global_variables_initializer().run()
	# train()
	restore()
	embeddings=np.array(sess.run(embeddings))
	