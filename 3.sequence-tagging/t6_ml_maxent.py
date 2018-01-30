# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

from time import time
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
# also see
#from nltk.classify.maxent import MaxentClassifier

class POSTagger():
    
    def __init__(self):
        
        # logistic regression / maximum entropy classifier
        self.tagger = LogisticRegression()
        self.vectorizer = DictVectorizer()
        
    def word2features(self, sent, i):
        features = {}
        features['word'] = sent[i][0].lower()      
        if i > 0:
            features['pos_p'] = sent[i-1][1]
        else:
            features['pos_p'] = 'BGN'
                    
        return features

    def sent2features(self, sent):
        return [self.word2features(sent, i) for i in range(len(sent))]
    
    # token, postag, label in sent
    def sent2tags(self, sent):
        return [tag for _, tag, _ in sent]
    
    def sent2tokens(self, sent):
        return [token for token, _, _ in sent]
    
    def train(self, sents):
        start = time()
        
        training_features = []
        training_labels = []
        for s in sents:
            training_features.extend(self.sent2features(s))
            training_labels.extend(self.sent2tags(s))
            
        t = time()
        print t-start, 'features extracted'
        
        train_matrix = self.vectorizer.fit_transform(training_features)
        # self.vectorizer.fit(training_features)
        # self.vectorizer.transform(training_features)
        # print self.vectorizer.get_feature_names()
        
        t = time()
        print t-start, 'features vectorized'
        
        self.tagger.fit(train_matrix, training_labels)
        
        t = time()
        print t-start, 'model trained'
    
    def tag_sent(self,sent):
        tags = ['BGN']
        for i in range(len(sent)):
            # make a list
            f = [{'word':sent[i], 'pos_p':tags[i]}]
            X = self.vectorizer.transform(f)
            # takes a list of lists and returns a list
            # only one item, get 0, 
            # keep the tag and use for the next word
            tags.append( self.tagger.predict(X)[0] )
            
        return tags
    
    def test(self, sents):
        '''
        test the sentences while tagging them
        '''
        test_sents = [self.sent2tokens(s) for s in sents]
        y_true = []
        for s in sents:
            y_true.extend(self.sent2tags(s))
        
        y_pred = []
        for sent in test_sents:
            # skip the 'BGN' tag
            y_pred.extend( self.tag_sent(sent)[1:] )
        
        print y_true[:10]
        print y_pred[:10]
        
        
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        accuracy = accuracy_score(y_true, y_pred)
        
        return [precision, recall, f1, accuracy]
    
    def test_2(self, sents):
        '''
        test every word individually as you know the previous pos tag
        not in real life
        '''
        test_features = []
        y_true = []
        for s in sents:
            test_features.extend(self.sent2features(s))
            y_true.extend(self.sent2tags(s))
        
        test_matrix = self.vectorizer.transform(test_features)
        
        y_pred = self.tagger.predict(test_matrix)
        
        print y_true[:10]
        print y_pred[:10]
        
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        accuracy = accuracy_score(y_true, y_pred)
        
        return [precision, recall, f1, accuracy]


if __name__ == '__main__':
    
    tr = open('data/conll_2000_train.txt', 'r')
    train_sents = [[w.split() for w in sent.strip().split('\n')] for sent in tr.read().strip().decode('utf-8').split('\n\n') if len(sent) and len(sent[0])]
    tr.close()
    
    ts = open('data/conll_2000_test.txt', 'r')
    test_sents = [[w.split() for w in sent.strip().split('\n')] for sent in ts.read().strip().decode('utf-8').split('\n\n') if len(sent) and len(sent[0])]
    ts.close()
    
    tagger = POSTagger()
    tagger.train(train_sents)
    print tagger.test(test_sents)
    print tagger.test_2(test_sents)
    
    sent = ['This', 'is', 'a', 'test', 'sentence', '.']
    print sent
    print tagger.tag_sent(sent)[1:]