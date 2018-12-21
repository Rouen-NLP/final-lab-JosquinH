## Classification des documents du procès des groupes américains du tabac

### Contexte

Le but de ce projet est de classer un ensemble de 3482 documents textes répartis en 10 classes : 

 - Form : 431
 - News : 188
 - Letter : 567
 - Resume : 120
 - Scientifique : 261 
 - Memo : 620
 - Note : 201
 - Advertisement : 230 
 - Report : 265
 - Email : 599

La répartition de ces données est donc assez hétérogènes, avec 5 fois plus d'email que de resume.

### Solution

Durant ce projet la solution retenue est de tout d'abord utiliser un bag of word pour transformer en vecteur de flottant l'ensemble des documents texte. Cette permet d'associer à chaque type de document un histogramme type des mots les plus utilisé et ainsi facilité le rapprochement entre les documents de même classe.

Ensuite la méthode de classification retenue est le SVM, qui permet un bon compromis entre temps d'apprentissage/éxécution et performances.

Le SVM à été entrainé sur 80% des données. Un ensemble de test sur les hypers-paramètres a de plus été effectué sur :

. Le noyau ( Radial basis function ou polynomial ).
. Le gammma pour le noyau rbf
. Le degree pour le noyau polynomial


### Analyse des performances

Après plusieurs tests, le noyau rbf semble être le plus performant sur ce problème avec un score moyen 0.70.

Avec le meilleur gamma trouvé à 0.001 on obtient les résultats suivant : 

0 -> Form
1 -> News
2 -> Letter
3 -> Resume
4 -> Scientific
5 -> Memo
6 -> Note
7 -> Advertisement
8 -> Report
9 -> Email

                  precision    recall  f1-score   support

           0       0.70      0.74      0.72        88
           1       0.88      0.68      0.77        34
           2       0.73      0.80      0.76       122
           3       1.00      1.00      1.00        15
           4       0.64      0.34      0.44        53
           5       0.66      0.80      0.72       109
           6       0.30      0.81      0.44        36
           7       1.00      0.16      0.27        57
           8       0.57      0.42      0.48        48
           9       0.95      0.92      0.94       135

    micro avg       0.70      0.70      0.70       697
    macro avg       0.74      0.66      0.65       697
    weighted avg       0.75      0.70      0.69       697


    69   0   2   0   0   4  12   0   0   1
     3  25   0   0   2   2   1   0   1   0
     4   0  94   0   0  20   1   0   3   0
     0   0   0  15   0   0   0   0   0   0
    11   0   4   0  18  10   3   0   7   0
     1   1  11   0   1  86   1   0   2   6
     3   0   1   0   0   2  30   0   0   0
     4   1   3   0   0   0  40   6   2   1
     6   2  16   0   3   4   0   0  17   0
     0   0   3   0   0   5   3   0   0 124


On peut noté une bonne précision sur l'ensemble des classes sauf pour Note et un mauvais recall pour Scientific et Report.