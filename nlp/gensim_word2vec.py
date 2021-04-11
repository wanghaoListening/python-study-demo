from gensim.models import word2vec
from gensim.models import KeyedVectors

# 加载语料
sentences = word2vec.Text8Corpus('/Users/didi/paper_code/分词后的天龙八部.txt')

# 训练模型
model = word2vec.Word2Vec(sentences)

vector = model.wv['computer']  # get numpy vector of a word


sims = model.wv.most_similar('computer', topn=10)  # get other similar words


# Store just the words + their trained embeddings.
word_vectors = model.wv
word_vectors.save("word2vec.wordvectors")

# Load back with memory-mapping = read-only, shared across processes.
wv = KeyedVectors.load("word2vec.wordvectors", mmap='r')
vector = wv['computer']  # Get numpy vector of a word