import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score
#import re


read_file = pd.read_csv(r"E:\Soham\Study\TRF\Level 2\July 2019 Workshop\Task 3\Datasets\dataset_2\full.csv", names = ["liked", "text"] )
#print(read_file.head())

nltk.download("stopwords")

stop_words_set = set(stopwords.words("english"))
vectorizer = TfidfVectorizer(use_idf = True, lowercase=True, strip_accents="ascii", stop_words=stop_words_set, ngram_range=(2,2))

y = read_file.liked
x = vectorizer.fit_transform(read_file.text)

#print (x.shape)
#print (y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(x, y ,train_size= 0.8,  random_state=0)

#print(vectorizer)

clf = naive_bayes.MultinomialNB()
clf.fit(X_train,Y_train)

#print(roc_auc_score(Y_test, clf.predict_proba(X_test)[:,1]))


variable1 = np.array([input("Enter something: ")])
variable2 = vectorizer.transform(variable1)
if(clf.predict(variable2)[0] == 1):
    print("Positive Statement")
else:
    print("Negative or Neutral Statement")