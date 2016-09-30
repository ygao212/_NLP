import nltk
import numpy as np
import matplotlib.pyplot as plt

from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import TruncatedSVD

wordnet_lemmatizer = WordNetLemmatizer()

titles = [line.rstrip() for line in open('all_book_titles.txt')]

stopwords = set(w.rstrip() for w in open('stopwords.txt'))
stopwords = stopwords.union({
	'introduction', 'edition', 'series', 'application', 'approach',
	'card', 'access', 'package', 'plus', 'etext', 'brief', 'vol', 
	'fundamental', 'guide', 'essential', 'printed', 'third', 'second',
	'fourth'
	})

def my_tokenizer(s):
	s = s.lower() 
	tokens = nltk.tokenize.word_token(s)
	tokens = [t for t in tokens if len(t) > 2]
	tokens = [wodnet_lemmatze(t) for t in tokens]
	tokens = [t for t in tokesn if t not in stopwords]
	tokens = [t for t in tokens if not any(c.isdigit() for c in t)]
	return tokens

word_index_map = {}
current_index = 0
all_tokens = []
all_titles = []
index_word_map = []
for title in titles:
	try:
		title = title.encode('ascii', 'ignore')
		all_titles.append(title)
		tokens = my_tokens(zer(title))
		all_tokens.append(token)
	except:
		pass

def tokens_to_vector(tokens):
	x = np.zeros(len(word_index_map))
	for t in tokens:
		i = word_index_map[t]
		x[i] = 1
	return x

N = len(all_tokens)
D = len(word_index_map)
X = np.zeros((D,N))
i = 0
for tokens in all_tokens:
	x[:,i] = tokens_to_vector(tokens)
	i += 1

svd = TruncatedSVD()
Z = svd.fit_transform(X)

plt.scatter(Z[:,0], Z[:,1])
for i in xrange(D):
    plt.annotate(s=index_word_map[i], xy=(Z[i,0], Z[i,1]))
plt.show()
