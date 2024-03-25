# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 23:06:23 2019

@author: Ching
"""

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping

train_df = pd.read_csv('heart.csv')
print(train_df.head())

train_x=train_df.drop(['target'],axis=1)
print(train_x.head())

train_y = train_df[['target']]
print(train_y.head())

#create model
model = Sequential()
#get number of columns in training data
n_cols = train_x.shape[1]

#add model layers
model.add(Dense(200, activation = 'relu', input_shape=(n_cols,)))
model.add(Dense(200, activation = 'relu'))
model.add(Dense(200, activation = 'relu'))
model.add(Dense(1))

#compile model using mse as a measure of model performance
model.compile(optimizer = 'adam', loss = 'mean_squared_error')

early_stopping_monitor = EarlyStopping(patience = 3)

#train model
model.fit(train_x, train_y, validation_split = 0.2, epochs=30, callbacks=[early_stopping_monitor])

