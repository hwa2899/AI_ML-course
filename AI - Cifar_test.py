# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:32:05 2019

@author: Ching
"""

from keras.datasets import cifar10
(x_train,y_label_train),(x_test,y_label_test)=cifar10.load_data()
print("train data:",'images:',x_train.shape," labels:",y_label_train.shape)
print("test data:",'images:',x_test.shape ," labels:",y_label_test.shape)
label_dict={0:"airplane",1:"automobile",2:"bird",3:"cat",4:"deer", 5:"dog",6:"frog",7:"horse",8:"ship",9:"truck"}

import matplotlib.pyplot as plt
def plot_images_labels_prediction(images,labels,prediction, idx,num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num>25: num=25
    for i in range(0, num):
        ax=plt.subplot(5,5, 1+i)
        ax.imshow(images[idx])
        title=str(i)+','+label_dict[labels[i][0]]
        if len(prediction)>0:
            title+='=>'+label_dict[prediction[i]]
        ax.set_title(title,fontsize=10)
        ax.set_xticks([]);ax.set_yticks([])
        idx+=1
    plt.show()
plot_images_labels_prediction(x_test,y_label_test,[], 0,10)