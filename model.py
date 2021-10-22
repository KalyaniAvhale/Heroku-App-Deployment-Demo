# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:06:26 2021

@author: kalyani

In this file will perform feature engineering and train the model
"""

#import req libraries
import pandas as pd 
import numpy as np
import pickle

#read dataset
dataset = pd.read_csv('dataset.csv')

#fill nan values
dataset['experience'].fillna(0,inplace=True)

dataset['test_score'].fillna(dataset['test_score'].mean(),inplace=True)

#create X and Y (input and target features)
X = dataset.iloc[:,:3]
X.head()

#convert words to integer values
def convert_to_int(word):
    word_dict = {"zero": 0,"one":1,"two":2,"three":3,"four":4,"five":5,
                 "six":6,"seven":7,"eight":8,"nine":9,"ten":10,0:0,
                 "eleven":11,"twelve": 12}
    return word_dict[word]

X['experience'] = X['experience'].apply(lambda x: convert_to_int(x))

y = dataset.iloc[:,-1]

#model training
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,y)

print(model.score(X,y))

#saving model to disk
pickle.dump(model,open('model.pkl','wb'))

#Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2,9,6]]))



