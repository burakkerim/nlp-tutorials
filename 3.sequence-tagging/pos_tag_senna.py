# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

from nltk.tokenize import WordPunctTokenizer
from nltk.tag import SennaTagger

# senna_path = 'D:/Workspace/Library/senna/'
senna_path = '/media/burak/Data/Workspace/Library/senna'

pos = SennaTagger(senna_path)
tokenizer = WordPunctTokenizer()


def tokenize(sent):
    return tokenizer.tokenize(sent.lower())


def tag(sent):
    return pos.tag(tokenize(sent))


sentence = 'This sentence is a test sentence for test in a test environment.'

print(tokenize(sentence))
print(tag(sentence))
