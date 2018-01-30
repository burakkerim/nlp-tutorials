# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

from nltk.tokenize import wordpunct_tokenize
from nltk.tag import StanfordPOSTagger

# May need to export JAVA_HOME,
# use export in linux in a decent way 
import os
java_path = 'C:\Program Files\Java\jre1.8.0_25'
os.environ['JAVAHOME'] = java_path

tagger_home = 'D:/Workspace/Library/JavaNLP/stanford-postagger-full-2015-12-09/'
model = tagger_home + 'models/english-bidirectional-distsim.tagger'
jar_file = tagger_home + 'stanford-postagger.jar'

tagger = StanfordPOSTagger(model, path_to_jar=jar_file)

sentence = 'This sentence is a test sentence for test in a test environment.'

print tagger.tag( wordpunct_tokenize(sentence))
