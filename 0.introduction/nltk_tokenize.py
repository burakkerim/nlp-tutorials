# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

import os
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.tokenize.stanford import StanfordTokenizer

java_path = '/usr/lib/jvm/jdk1.8.0_31'

tagger_home = '/media/burak/Data/Workspace/Library/'\
              'stanford-postagger-full-2018-02-27/'

model = tagger_home + 'models/english-bidirectional-distsim.tagger'

jar_file = tagger_home + 'stanford-postagger.jar'

# print(os.environ['PATH'])
# print(type(os.environ['PATH']))

os.environ['JAVAHOME'] = os.environ.get(
    'JAVAHOME', '') + os.pathsep + java_path
os.environ['CLASSPATH'] = os.environ.get(
    'CLASSPATH', '') + os.pathsep + jar_file

tokenizer = StanfordTokenizer(path_to_jar=jar_file)

s1 = "On a $50,000 mortgage of 30 years at 8 percent,"
" the monthly payment would be $366.88."

s2 = "\"We beat some pretty good teams to get here.\" Slocum said."

s3 = "Well, we couldn't have this predictable, cliche-ridden, "
"\"Touched by an Angel\" "
"(a show creator John Masius worked on) wanna-be if she didn't."

s4 = "I cannot work under these conditions!"

s5 = "The company spent $30,000,000 last year."

p = [s1, s2, s3, s4, s4]
par = ' '.join(p)


for s in p:
    print(word_tokenize(s))
    print(wordpunct_tokenize(s))
    print(tokenizer.tokenize(s))
    print()

for s in sent_tokenize(par):
    print(word_tokenize(s))
    print(wordpunct_tokenize(s))
    print(tokenizer.tokenize(s))
    print()
