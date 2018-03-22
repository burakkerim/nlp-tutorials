# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

import os
from nltk.tag import StanfordNERTagger

java_path = '/usr/lib/jvm/jdk1.8.0_31'

ner_home = '/media/burak/Data/Workspace/Library/'\
           'stanford-ner-2018-02-27/'
model = ner_home + 'classifiers/english.all.3class.distsim.crf.ser.gz'
jar_file = ner_home + 'stanford-ner.jar'

os.environ['JAVAHOME'] = java_path
os.environ['CLASSPATH'] = jar_file
os.environ['STANFORD_MODELS'] = ner_home + 'classifiers/'

ner = StanfordNERTagger(model, jar_file)

sent = ['Sao', 'Paulo', '(', 'Brasil', ')', ',',
        '23', 'may', '(', 'EFECOM', ')', '.']

print(ner.tag(sent))
