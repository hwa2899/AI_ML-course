# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:12:16 2019

@author: Ching
"""

import numpy as np
import pandas as pd 
from keras.utils import np_utils
from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2,2)
    plt.imshow(image,cmap = 'binary')
    plt.show()
    
def plot_images_labels_prediction(images, labels, prediction, idx, num = 10):
    fig = plt.gcf()
    fig.set_size_inches(12,14)
    if num >25:
        num =25
    for i in range(0,num):
        ax = plt.subplot(5,5,1+i)
        ax.imshow(images[idx], cmap = 'binary')
        title = 'label=' + str(labels[idx])
        if len(prediction)>0:
            title += ",predict=" + str(prediction[idx])
        ax.set_title(title,fontsize = 20)
        idx += 1
    plt.show()

(x_train_image, y_train_label),(x_test_image, y_test_label) = mnist.load_data()

print('train data = ', len(x_train_image))
print('test data = ', len(x_test_image))
print('x_train_image:', x_train_image.shape)
print('y train image:' , y_train_label.shape)
print('x test image' , x_test_image.shape)
print('y test label' , y_test_label.shape)

x_train_image[0]

plot_image(x_train_image[0])
y_train_label[0]

plot_images_labels_prediction(x_train_image, y_train_label,[],0,10)

#--------------------------------------------------------------------
#practice 2 
x_Train = x_train_image.reshape(60000, 784).astype('float32')
x_Test = x_test_image.reshape(10000,784).astype('float32')
x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255
y_Train_Onehot = np_utils.to_categorical(y_train_label)
y_Test_Onehot = np_utils.to_categorical(y_test_label)

model = Sequential()
model.add(Dense(units=256, input_dim=784, kernel_initializer = 'normal', activation = 'relu'))
model.add(Dense(units=10, kernel_initializer = 'normal', activation = 'softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

model.fit(x = x_Train_normalize, y=y_Train_Onehot, validation_split = 0.2, epochs=10, batch_size=200, verbose=2)

prediction = model.predict_classes(x_Test)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx = 0)
