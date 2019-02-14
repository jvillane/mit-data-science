path_to_mitie_lib = './MITIE/mitielib'
path_to_ner_model = './MITIE/MITIE-models/spanish/ner_model.dat'

import sys
import numpy as np
from nltk import word_tokenize

sys.path.append(path_to_mitie_lib)
sys.path.append(path_to_ner_model)

# in MITIE/mitielib run 'make'
# in MITIE run 'make MITIE-models'
# for spanish download 'https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2-Spanish.zip'

from mitie import *

# total number of articles to process
N = 63
# in memory stores for the topics, titles and contents of the news stories
# topics_array = []
titles_array = []
corpus = []

for i in range(1, N):
    # get the contents of the article
    with open('./files/article-' + str(i) + '.txt', 'r') as myfile:
        d1 = myfile.read().replace('\n', '')
        d1 = d1.lower()
        corpus.append(unicode(d1, errors='replace'))
    # get the original topic of the article
    # with open('.files/topic-' + str(i) + '.txt', 'r') as myfile:
    #     to1 = myfile.read().replace('\n', '')
    #     to1 = to1.lower()
    #     topics_array.append(to1)
    # get the title of the article
    with open('./files/title-' + str(i) + '.txt', 'r') as myfile:
        ti1 = myfile.read().replace('\n', '')
        ti1 = ti1.lower()
        titles_array.append(ti1)

ner = named_entity_extractor(path_to_ner_model)

# entity subset array
entity_text_array = []
for i in range(0, N-1):
    # Load the article contents text file and convert it into a list of words.
    print i
    tokens = word_tokenize(corpus[i])
    # extract all entities known to the ner model mentioned in this article
    entities = ner.extract_entities(tokens)
    # extract the actual entity words and append to the array
    for e in entities:
        range_array = e[0]
        tag = e[1]
        score = e[2]
        score_text = "{:0.3f}".format(score)
        entity_text = " ".join(tokens[j] for j in range_array)
        entity_text_array.append(entity_text.lower())

# remove duplicate entities detected
entity_text_array = np.unique(entity_text_array)

# ###### #
# TF-IDF #
# ###### #

from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', stop_words='english', vocabulary=entity_text_array)
corpus_tf_idf = vect.fit_transform(corpus)

# ################### #
# SPECTRAL CLUSTERING #
# ################### #

from sklearn import cluster
# change n_clusters to equal the number of clusters desired
n_clusters = 7
n_components = n_clusters
#spectral clustering
spectral = cluster.SpectralClustering(n_clusters= n_clusters, eigen_solver='arpack', affinity="nearest_neighbors", n_neighbors = 10)
spectral.fit(corpus_tf_idf)

if hasattr(spectral, 'labels_'):
    cluster_assignments = spectral.labels_.astype(np.int)
for i in range(0, len(cluster_assignments)):
    # print (i, topics_array[i], cluster_assignments [i], titles_array[i])
    print (i, cluster_assignments [i], titles_array[i])
