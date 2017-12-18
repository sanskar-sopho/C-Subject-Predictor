from gensim.models import Word2Vec
from nltk.corpus import brown

model=Word2Vec(brown.sents())
print(model.most_similar('money',topn=5))

