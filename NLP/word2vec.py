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
			save_path=saver.save(sess,'restore/model.ckpt')
			print "Successfully saved in ",save_path	
	save_path=saver.save(sess,'restore/model.ckpt')
	print "Successfully saved in ",save_path

def restore():
	saver=tf.train.Saver([embeddings,soft_weights,soft_biases])
	# tf.reset_default_graph()
	saver.restore(sess,"restore/model.ckpt")
	print "Successfully Restored"


with tf.Session() as sess:
	tf.global_variables_initializer().run()
	# train()
	restore()
	# print(sess.run(loss,feed_dict={X:train_x,Y:train_y}))
	embeddings=np.array(sess.run(embeddings))
	print embeddings[3]



# We have word2vec, now defining RNN
# 0 Memory 1 Operation 2 Algorithm 3 Concurrency
data=['assign','memory','contiguous','allocated','storage','file handl','sub problem','iterative sort','bucket sort','insertion sort','merge sort','replace','puts','gets','declaration','initialisation','Step','insert','select','insert','add','delete','deadlock','livelock','synchronisation','data race']
labels=[0,0,0,0,0,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3]


n_steps=3
n_feature=embed_size
n_neurons=45
n_class=4
l_rate=0.001
num_iter=1000

X_=[]
for element in data:
	words=element.split()
	i=0
	for word in words:
		X_.append(embeddings[word2int[word]])
		i+=1
	while(i<n_steps):
		X_.append([0 for j in range(0,n_feature)])
		i+=1

X_=np.array(X_)
Y_=[]
for label in labels:
	Y_.append([(1 if i==label else 0) for i in range(0,n_class)])
Y_=np.array(Y_)
print(X_.shape,Y_.shape)

X_=X_.reshape((-1,n_steps,n_feature))
Y_=Y_.reshape((-1,n_class))

print X_.shape,Y_.shape
tf.reset_default_graph()

X=tf.placeholder(tf.float32,[None,n_steps,n_feature])
Y=tf.placeholder(tf.int32,[None,n_class])

basic_cell=tf.nn.rnn_cell.BasicLSTMCell(num_units=n_neurons)

outputs,states=tf.nn.dynamic_rnn(basic_cell,X,dtype=tf.float32)

outputs=tf.unstack(tf.transpose(outputs,perm=[1,0,2]))
last_output=outputs[-1]
print last_output

logits=fully_connected(last_output,n_class,activation_fn=None)
cross_entropy=tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=Y)

loss=tf.reduce_mean(cross_entropy)
train_step=tf.train.AdamOptimizer(l_rate).minimize(loss)

correct=tf.equal(tf.argmax(logits,1),tf.argmax(Y,1))
accuracy=tf.reduce_mean(tf.cast(correct,tf.float32))

def train_rnn():
	saver=tf.train.Saver()
	for i in range(0,num_iter):
		sess.run(train_step,feed_dict={X:X_,Y:Y_})
		if(i%50==0):
			print "loss is ",loss.eval(feed_dict={X:X_,Y:Y_})
	save_path=saver.save(sess,'rnn_saver/model.ckpt')
	print "Successfully saved in ",save_path

def restore_rnn():
	saver=tf.train.Saver()
	saver.restore('rnn_saver/model.ckpt')
	print "Successfully restored"

with tf.Session() as sess:
	tf.global_variables_initializer().run()
	# train_rnn()
	restore_rnn()
	print "Accuracy = ",accuracy.eval(feed_dict={X:X_,Y:Y_})