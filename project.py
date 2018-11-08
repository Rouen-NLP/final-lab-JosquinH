#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:28:33 2018

@author: havarjos
"""

import numpy as np
import pandas
import seaborn as sns
import csv

#%%%

"""
Recuperation des chemins d'acces des fichiers et des labels des fichiers
"""

file_list = []
label_list = []

with open('data/Tobacco3482.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', )
    line_count = 0
    for line in spamreader:
        if line_count != 0:
            file_name = line[0]
            file_name = file_name.replace('.jpg','.txt')
            file_list.append(file_name)
            label_list.append(line[1])
        line_count += 1

#%%%
        
"""
Les labels string sont remplace par des labels chiffres
"""

N = len(label_list)

"""
labels = list(set(file_label_list))

dico_labels = {}

for i in range(len(labels)):
    dico_labels[labels[i]] = i

y = np.zeros((N,1))

for i in range(N):
    y[i] = dico_labels[file_label_list[i]]
"""   

#%%%

list_text = []

for i in range(N):
    with open('data/'+file_list[i]) as my_file:
        my_str = ''
        for line in my_file:
            my_str += line
        list_text.append(my_str)
    if i % 100 == 0 :
        print(str(i) +' / '+str(N) + ' faits')

#%%%



