#! C:\Users\Asus-Pc\OneDrive - Universidad Politécnica de Madrid\Escritorio\python\myenv\Scripts\python.exe

import pandas as pd
import numpy as np
import math as m
import matplotlib.pyplot as mp

data_set_train=np.array(pd.read_csv('ItalyPowerDemand/ItalyPowerDemand_TRAIN.tsv',sep='\t'))
data_set_test=np.array(pd.read_csv('ItalyPowerDemand/ItalyPowerDemand_TEST.tsv',sep='\t'))
     # get the training data
train_data=data_set_train[:,1:]
train_classes=data_set_train[:,0]
print(train_data)
print(train_classes)
for i in range(0,len(train_data)):
    if train_classes[i] == 1:
        mp.plot(train_data[i,:],color='black')
    else:
        mp.plot(train_data[i,:],color='green')
mp.show()