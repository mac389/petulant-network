import random, itertools

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

topics = [['honey','badger','sniffles'],['honey','bunches','oats'],['cough','alpaca','llama']]


'''
	2. Project words onto topics, using Jaccard similarity
'''

corpus = [topics[0]*5,topics[1]*5,topics[-1]*5,random.sample(list(itertools.chain(*topics)),3)*5]
for document in corpus:
	print ' '.join(document)

topic_topic_similarities = np.array([[jaccard_similarity(topic_A,topic_B) for topic_A in topics] for topic_B in topics])
corpus_topic_similarities = np.array([[jaccard_similarity(text,topic) for text in corpus] for topic in topics])
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
plt.show()