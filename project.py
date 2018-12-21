#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:28:33 2018

@author: havarjos
"""

import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.svm import SVC
#%%%

"""
    Récupération des données
"""
df = pd.read_csv('data/Tobacco3482.csv')

file_name_path = df.img_path
N = len(file_name_path)
list_text = []

for i in range(N):
    file_name = file_name_path[i]
    file_name = file_name.replace('.jpg','.txt')
    with open('data/'+file_name) as my_file:
        my_str = ''
        for line in my_file:
            my_str += line
        list_text.append(my_str)
    if i % 100 == 0 :
        print(str(i) +' / '+str(N) + ' faits',end='\r')

print('Finit')

df['text'] = list_text

X = df.text

labels = list(set(df.label))
y = np.zeros(len(X),dtype='int')

for i in range(len(X)):
    y[i] = labels.index(df.label[i]) 
    

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#%%%

"""
    Transformation en BOW
"""

vectorizer = CountVectorizer(max_features=2000)
vectorizer.fit(X_train)
X_train_counts = vectorizer.transform(X_train)
X_test_counts = vectorizer.transform(X_test)

#%%%

"""
    Apprentissage
"""

t0 = time.time()

clf = SVC(gamma=0.001, kernel='rbf')

clf.fit(X_train_counts, y_train)

print('Apprentissage finit en : ' + str(time.time() - t0) + ' secondes')

#%%%

"""
    Test
"""

predict_label_counts = clf.predict(X_test_counts)

class_counts = classification_report(y_test,predict_label_counts) 

matrice_counts = confusion_matrix(y_test,predict_label_counts)

print(class_counts)
print(matrice_counts)



