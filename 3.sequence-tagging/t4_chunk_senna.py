# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

from nltk.tokenize import WordPunctTokenizer
from nltk.tag import SennaChunkTagger

senna_path = 'D:/Workspace/Library/senna/'

chunker = SennaChunkTagger(senna_path)
tokenizer = WordPunctTokenizer()


def tokenize(sent):
    return tokenizer.tokenize(sent.lower())

def chunk(sent):
    return chunker.tag(tokenize(sent))

sentence = 'This sentence is a test sentence for test in a test environment.'

print tokenize(sentence)
print chunk(sentence)
