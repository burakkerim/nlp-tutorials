# -*-coding: utf-8 -*-
'''
Created on 17 Mar 2016

@author: BurakKerim
'''

# -*- coding: utf-8 -*-
'''
Created on 9 May 2015

@author: BurakKerim
'''

from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from nltk import wordpunct_tokenize as tokenize
import pickle

### HELPER FUNCTION & VARIABLES ###
case_suffixes = ['i','ı','e','a','de','da','den','dan','in','ın','ün','un',
                 'yi','yı','ye','ya','nde','nda','nden','ndan','nin','nın','nün','nun',]

stop_words = ['acaba', 'ama', 'asl\xc4\xb1nda', 'az', 'baz\xc4\xb1', 'belki', 'biri', 
              'birka\xc3\xa7', 'bir\xc5\x9fey', 'biz', 'bu', '\xc3\xa7ok', 
              '\xc3\xa7\xc3\xbcnk\xc3\xbc', 'da', 'daha', 'de', 'defa', 'diye', 
              'e\xc4\x9fer', 'en', 'gibi', 'hem', 'hep', 'hepsi', 'her', 'hi\xc3\xa7', 
              'i\xc3\xa7in', 'ile', 'ise', 'kez', 'ki', 'kim', 'm\xc4\xb1', 'mu', 
              'm\xc3\xbc', 'nas\xc4\xb1l', 'ne', 'neden', 'nerde', 'nerede', 'nereye', 
              'ni\xc3\xa7in', 'niye', 'o', 'sanki', '\xc5\x9fey', 'siz', '\xc5\x9fu', 
              't\xc3\xbcm', 've', 'veya', 'ya', 'yani']

skip_list = stop_words + case_suffixes + []

def valid(token):
    if token.isalnum() and token not in skip_list:
        return True
    else:
        return False 

class Classifier():
    
    def __init__(self):
        
        self.cls1 = SVC(kernel='linear',probability=True)
        self.cls2 = MultinomialNB(fit_prior=False)
        self.cls3 = KNeighborsClassifier()
        self.vectorizer = TfidfVectorizer(min_df=1)
        self.is_trained = False
        
    def train(self, filenames):
        files = open(filenames, 'r')
        self.train_([f for f in files])
        
    def train_(self, files):
        training_corpus = []
        training_labels = []
        for f in files:
            f_name = f.split('\t')[0].strip()
            cat = f.split('\t')[1].strip()
            f = open(f_name,'r')
            tokens = ' '.join([t.lower()[:5] for t in tokenize(f.read()) if valid(t)])
            f.close()
            training_corpus.append(tokens)
            training_labels.append(cat)
        
        train_vectors = self.vectorizer.fit_transform(training_corpus)
        
        self.cls1.fit(train_vectors, training_labels)
        self.cls2.fit(train_vectors, training_labels)
        self.cls3.fit(train_vectors, training_labels)
        
        self.is_trained = True
    
    def test(self, filenames):
        if not self.is_trained:
            print 'Train the classifier or load a model'
            return
        files = open(filenames, 'r')
        return self.test_([f for f in files])
    
    def test_(self, files):
        test_corpus = []
        test_labels = []
        for f in files:
            f_name = f.split('\t')[0].strip()
            cat = f.split('\t')[1].strip()
            f = open(f_name,'r')
            tokens = ' '.join([t[:5] for t in tokenize(f.read()) if valid(t)])
            f.close()
            test_corpus.append(tokens)
            test_labels.append(cat)
        
        test_vector = self.vectorizer.transform(test_corpus)
        
        # just to order matrix
        #classes = ['POLITICS', 'ECONOMICS', 'SCIENCE', 'CULTURE', 'SPORTS']
        
        p1 = self.cls1.predict(test_vector)
        a1 = accuracy_score(test_labels, p1)
        #c1 = confusion_matrix(test_labels, p1, classes)
        
        p2 = self.cls2.predict(test_vector)
        a2 = accuracy_score(test_labels, p2)
        #c2 = confusion_matrix(test_labels, p2, classes)
        
        p3 = self.cls3.predict(test_vector)
        a3 = accuracy_score(test_labels, p3)
        #c3 = confusion_matrix(test_labels, p3, classes)
        
        p1 = self.cls1.predict_proba(test_vector)
        p2 = self.cls2.predict_proba(test_vector)
        p3 = self.cls3.predict_proba(test_vector)
        p4 = p1+p2+p3 / 3
        
        p4 = [self.cls1.classes_[x.tolist().index(max(x))] for x in p4]
                
        a4 = accuracy_score(test_labels, p4)
        #c4 = confusion_matrix(test_labels, p4, classes)
        
        #return [(a1,c1), (a2,c2), (a3,c3), (a4,c4)]
        return [a1,a2,a3,a4]
        
    def save(self, filename):
        if not self.is_trained:
            print 'Train the classifier or load a model'
            return
        
        models = [self.cls1, self.cls2, self.cls3, self.vectorizer]
        f = open(filename, 'wb')
        pickle.dump(models, f)
        f.close()
        
    def load(self, filename):
        f = open(filename)
        [self.cls1, self.cls2, self.cls3, self.vectorizer] = pickle.load(f)
        f.close()
        self.is_trained = True

if __name__ == '__main__':
    
    cls = Classifier()
    cls.train('data/training.txt')
    print cls.test('data/test.txt')
    cls.save('data/model.pkl')
    print cls
    del cls
    try: 
        print cls
    except:
        print 'no cls'
    
    cls = Classifier()
    cls.load('data/model.pkl')
    print cls.test('data/test.txt')
    