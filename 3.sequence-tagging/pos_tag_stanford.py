# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

from nltk.tokenize import wordpunct_tokenize
from nltk.tag import StanfordPOSTagger
from nltk.tokenize.stanford import StanfordTokenizer

# May need to export JAVA_HOME,
# use export in linux in a decent way
import os

java_path = '/usr/lib/jvm/jdk1.8.0_31'
# java_path = 'C:\Program Files\Java\jdk1.8.0_31'

os.environ['JAVAHOME'] = java_path

tagger_home = '/media/burak/Data/Workspace/Library/'\
              'stanford-postagger-full-2018-02-27/'

model = tagger_home + 'models/english-bidirectional-distsim.tagger'

jar_file = tagger_home + 'stanford-postagger.jar'

tagger = StanfordPOSTagger(model, path_to_jar=jar_file)
tokenizer = StanfordTokenizer(path_to_jar=jar_file)

sentence = 'This sentence is a test sentence for test in a test environment.'

print(tagger.tag(wordpunct_tokenize(sentence)))
print(tagger.tag(tokenizer.tokenize(sentence)))
