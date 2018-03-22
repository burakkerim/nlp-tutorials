# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

from nltk.tag import SennaNERTagger

senna_path = '/media/burak/Data/Workspace/Library/senna'

ner = SennaNERTagger(senna_path)

sent = ['Sao', 'Paulo', '(', 'Brasil', ')', ',',
        '23', 'may', '(', 'EFECOM', ')', '.']

print(ner.tag(sent))
