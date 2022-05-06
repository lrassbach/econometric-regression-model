# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:21:06 2020

@author: lrass
"""
import csv

original_csv = open('New_Users_June_2020.csv','r')
reader = csv.reader(original_csv)
original_csv= reader

front="'"
back="'"
comma=','

new_csv = open('new_users_june_2020_sqlrdy.csv','w')
for item in original_csv:
    b = str(item)
    a = str(b)[1:-1]
    #a = front+b+back
    new_csv.write(a+','+"\n")


    

