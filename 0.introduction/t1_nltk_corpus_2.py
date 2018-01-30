# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

from nltk.corpus import names, stopwords
from nltk.corpus import brown
from nltk.corpus import conll2000, conll2002
from nltk.corpus import treebank

# NAMES
print 'NAMES:', len(names.words()), len(names.words('female.txt')), len(names.words('male.txt'))
print names.words('female.txt')[:10]
print names.words('male.txt')[:10]
print

# STOPWORDS
print 'STOPWORD LANGUAGES:'
print stopwords.fileids()
print 'English stopwords', len(stopwords.words('english'))
print stopwords.words('english')[:20]
print 'Turkish stopwords', len(stopwords.words('turkish'))
print stopwords.words('turkish')[:20]
print

# TAGGED
# remember categories and fileids
# print brown.categories()
# print brown.words(categories='news')
# print brown.sents(categories=['news', 'editorial', 'reviews'])
print 'POS TAGS:'
print 'WORDS:'
print brown.words()[:5]
print brown.tagged_words()[:5]
print 'SENTS:'
print [s[:5] for s in brown.sents()[:5]]
print [s[:5] for s in brown.tagged_sents()[:5]]
print

# CHUNKED
#The CoNLL 2000 Corpus includes phrasal chunks; and the CoNLL 2002 Corpus includes named entity chunks
print 'CHUNKING & NER:'
print conll2000.fileids()
print conll2000.sents()[0]
print conll2000.chunked_sents()[0]
print conll2002.sents()[0]
print conll2002.chunked_sents()[0]
print

# PARSED
# 10% sample of the Penn Treebank
print 'PENN TREEBANK:'
print treebank.fileids()[:5]
print treebank.words('wsj_0001.mrg')[:10]
print treebank.tagged_words('wsj_0001.mrg')[:10]
print treebank.sents('wsj_0001.mrg')[0]
print treebank.parsed_sents('wsj_0001.mrg')[0]
print