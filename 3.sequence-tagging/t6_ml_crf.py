# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

from sklearn.metrics import f1_score
import sklearn_crfsuite

def word2features(sent, i):
    '''
    return feature dictionary
    '''
    word = sent[i][0]
    postag = sent[i][1]
    
    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'postag': postag,        
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:postag': postag1,
        })
    else:
        # beginning of the sentence
        features['BOS'] = True
        
    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:postag': postag1,
        })
    else:
        # end of the sentenece
        features['EOS'] = True
                
    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

# token, postag, label in sent
def sent2labels(sent):
    return [label for _, _, label in sent]

def sent2tokens(sent):
    return [token for token, _, _ in sent]


tr = open('data/conll_2000_train.txt', 'r')
train_sents = [[w.split() for w in sent.strip().split('\n')] for sent in tr.read().strip().decode('utf-8').split('\n\n') if len(sent) and len(sent[0])]
tr.close()

ts = open('data/conll_2000_test.txt', 'r')
test_sents = [[w.split() for w in sent.strip().split('\n')] for sent in ts.read().strip().decode('utf-8').split('\n\n') if len(sent) and len(sent[0])]
ts.close()

# see what kind of features are returned
print 'FEATURE EXAMPLE:'
print sent2features(train_sents[0])[0]

X_train = [sent2features(s) for s in train_sents]
y_train = [sent2labels(s) for s in train_sents]

X_test = [sent2features(s) for s in test_sents]
y_test = [sent2labels(s) for s in test_sents]

print 'training...'
crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=100,
    all_possible_transitions=True
)

crf.fit(X_train, y_train)


labels = list(crf.classes_)
print 'LABELS:'
print labels

y_pred = crf.predict(X_test)
print f1_score(y_test, y_pred, average='micro')
