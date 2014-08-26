import json, itertools

import matplotlib.pyplot as plt

filename = '../data/lda_topics.json'
READ = 'rb'

data = json.load(open(filename,READ))


#create matrix to display
words = list(set(itertools.chain(*[data[topic].keys() for topic in data])))    
as_grid = [[data[topic][word] if word in data[topic] else 0 for topic in data] for word in words]

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(as_grid,interpolation='nearest',aspect='auto',cmap=plt.cm.binary)
cbar = plt.colorbar(cax)
cbar.set_label('$\phi$', rotation='horizontal')
ax.set_yticks(xrange(len(words)))
ax.set_yticklabels(words)
ax.set_xlabel('Topic No.')
# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.grid(True)
plt.tight_layout()
plt.savefig('../data/lda_topics.png',dpi=300)