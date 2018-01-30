# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

import nltk
from nltk.book import gutenberg as gutenber_book
from nltk.corpus import brown, gutenberg

nltk.corpus.gutenberg.fileids()

#-------------------------
# Accessing Text Corpora
#-------------------------

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
emma = nltk.Text(emma)
emma.concordance("surprize")

# Gutenberg Corpus

macbeth_sentences = gutenber_book.sents('shakespeare-macbeth.txt')
print len(macbeth_sentences), 'sentences in Macbeth'
print 'SENT EXAMPLE: ',macbeth_sentences[1037]
longest_len = max([len(s) for s in macbeth_sentences])
print longest_len
print [s for s in macbeth_sentences if len(s) == longest_len]

macbeth_raw = gutenber_book.raw('shakespeare-macbeth.txt')
macbeth_words = gutenber_book.words('shakespeare-macbeth.txt')

print 'LENGTHS'
print 'RAW:', len(macbeth_raw)
print 'WORDS:', len(macbeth_words)
print 'SENTS:', len(macbeth_sentences)

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid

# Brown Corpus    

print brown.categories()
print brown.words(categories='news')
print brown.words(fileids=['cg22'])
print brown.sents(categories=['news', 'editorial', 'reviews'])

news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
whs = ['what', 'when', 'where', 'who', 'why']
for m in modals:
    print m + ':', fdist[m],
print #newline
for m in whs:
    print m + ':', fdist[m],
print '\n'   
cfd = nltk.ConditionalFreqDist(
           (genre, word)
           for genre in brown.categories()
           for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)
