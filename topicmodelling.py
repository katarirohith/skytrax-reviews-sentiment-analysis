import string
import gensim
from gensim import corpora
import csv
import pandas as pd
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()


def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


df = pd.read_csv(os.path.expanduser(r"~/Desktop/670projectdata/emirates.csv"), encoding='unicode_escape', sep=",")
Topic = []
i = 0
for rows in df.Reviews:

    if __name__ == '__main__':
        doc_complete = rows.split(',')
        doc_clean = [clean(doc).split() for doc in doc_complete]
        dictionary = corpora.Dictionary(doc_clean)
        doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
        Lda = gensim.models.ldamodel.LdaModel
        ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)
        t = ldamodel.print_topics(num_topics=1, num_words=15)
        Topic.append(t)
        i += 1
        print(i)


if __name__ == '__main__':

    df['Topic'] = Topic
    df.to_csv(os.path.expanduser(r"~/Desktop/670projectdata/emirates.csv"),index=False)

