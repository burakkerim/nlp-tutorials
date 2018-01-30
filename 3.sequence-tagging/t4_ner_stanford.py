# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

import os
from nltk.tag import StanfordNERTagger

# May need to export JAVA_HOME,
# use export in linux in a decent way 
java_path = 'C:\Program Files\Java\jre1.8.0_25'

ner_home = 'D:/Workspace/Library/JavaNLP/stanford-ner-2015-12-09/'
model = ner_home + 'classifiers/english.all.3class.distsim.crf.ser.gz'
jar_file = ner_home + 'stanford-ner.jar'

os.environ['JAVAHOME'] = java_path
os.environ['CLASSPATH'] = jar_file
os.environ['STANFORD_MODELS'] = ner_home + 'classifiers/'

ner = StanfordNERTagger(model, jar_file)

sent = ['Sao', 'Paulo', '(', 'Brasil', ')', ',', '23', 'may', '(', 'EFECOM', ')', '.']

print ner.tag(sent)
