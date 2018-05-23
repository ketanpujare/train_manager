# -*- coding: utf-8 -*-

from csv import reader
import os

files = os.listdir('Data/train_timetable/')

for train in files:
    with open('Data/train_timetable/'+train,'rb') as trainfile:
        read = reader(trainfile)
        tt = list(read) 
