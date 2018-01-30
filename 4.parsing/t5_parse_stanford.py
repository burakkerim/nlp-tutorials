# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

import os
from nltk.parse.stanford import StanfordParser, StanfordDependencyParser

java_path = 'C:\Program Files\Java\jre1.8.0_25'
parser_home = 'D:/Workspace/Library/JavaNLP/stanford-parser-full-2015-12-09/'
os.environ['JAVAHOME'] = java_path
os.environ['STANFORD_PARSER'] = parser_home
os.environ['STANFORD_MODELS'] = parser_home

parser = StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
dep_parser = StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

parser = StanfordParser()
dep_parser = StanfordDependencyParser()

# see parse methods:
# raw_parse
# raw_parse_sents
# parse
# parse_one
# parse_all
# parse_sents
# use _sents for performance

sentence = 'This sentence is a test sentence for test in a test environment.'

for parse in parser.raw_parse(sentence):
    print parse
print

for parse in dep_parser.raw_parse(sentence):
    print parse.tree()
print

for sent in dep_parser.raw_parse_sents([sentence]):
    for parse in sent:
        for tri in parse.triples():
            print tri
    print
