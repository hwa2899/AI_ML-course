# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 23:06:23 2019

@author: Ching
"""

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from keras.utils import to_categorical

train_df_2 = pd.read_csv('heart.csv')
print(train_df_2.head())

train_x_2=train_df_2.drop(['target'],axis=1)
print(train_x_2.head())

#one-hot encode target column
train_y_2 = to_categorical(train_df_2.target)
train_y_2[0:5]

model_2 = Sequential()
n_cols_2 = train_x_2.shape[1]

model_2.add(Dense(250,activation = 'relu', input_shape=(n_cols_2,)))
model_2.add(Dense(250, activation = 'relu'))
model_2.add(Dense(2, activation='softmax'))

model_2.compile(optimizer = 'adam', loss='categorical_crossentropy', metrics=['accuracy'])

#early_stopping_monitor = EarlyStopping(patience=3)
#model_2.fit(train_x_2, train_y_2, epochs = 30, validation_split = 0.2, callbacks=[early_stopping_monitor])
#train model
model_2.fit(train_x_2, train_y_2, epochs=30, validation_split=0.2 )