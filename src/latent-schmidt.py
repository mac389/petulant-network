import random, itertools,json

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

def jaccard_similarity(a,b):
	a = set(a)
	b = set(b)
	return len(a&b)/float(len(a|b))

'''
   1. Get topics from corpus using gensim
'''

topics = json.load(open('../data/lda_topics.json','rb'))

'''
	2. Project words onto topics, using Jaccard similarity
'''

corpus = [line.strip() for line in open('../data/sample_topics','rb').read().splitlines()]

topic_topic_similarities = np.array([[jaccard_similarity(topics[topic_A],topics[topic_B]) for topic_A in topics] for topic_B in topics])
corpus_topic_similarities = np.array([[jaccard_similarity(text,topics[topic]) for text in corpus] for topic in topics])
'''
   3. Gram-Schmidt Orthogonalize (SciPy) and, identify clusters in this space 
      --generalized eigenvalues are better
'''

eigenvalues,eigenvectors = LA.eig(topic_topic_similarities) #symmetric left and right eigenvectors are the same
projections = eigenvectors.T.dot(corpus_topic_similarities).T #ijth entry denotes the projection of the ith piece of text onto the jth topic

'''
    4. Visuazlie
'''


fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(projections,interpolation='nearest',aspect='auto')

ax.set_xticks(range(projections.shape[1]))
ax.set_yticks(range(projections.shape[0]))
ax.set_xlabel('Principal components')
ax.set_ylabel('Piece of text')
cbar = plt.colorbar(cax)
cbar.set_label('Strength of projection')
plt.tight_layout()
plt.savefig('../data/lda_projections.png',dpi=300)