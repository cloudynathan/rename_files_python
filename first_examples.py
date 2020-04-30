# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:55:41 2020

@author: cloud
"""


import os

files = os.listdir('.')

myfiles = []
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      myfiles.append(os.path.join(root, name))
      
      
os.rename('Form_A100.txt','x_Form_A100.txt')


os.rename('files_1/file_1.txt','files_1/file_11.txt')


myfolder = 'files_1/hhhh'
files = os.listdir(myfolder)
for file in files:
    current = os.path.join(myfolder, file)
    
    items = file.split('_')
    items = [x.title() for x in items]
    newfile = '_'.join(items)
    
    new = os.path.join(myfolder, newfile)
    os.rename(current,new)
    
    
    
os.rename(file, file.lower())

##
myfolder = 'files_1'
files = os.listdir(myfolder)
for i, file in enumerate(files):
    current = os.path.join(myfolder, file)
    if os.path.isfile(current):
        new = os.path.join(myfolder, str(i+1) + '_' + file.lower())
        os.rename(current,new)
        
        
myfolder = 'files_1'
files = os.listdir(myfolder)
i = 1
for file in files:
    current = os.path.join(myfolder, file)
    if os.path.isfile(current):
        new = os.path.join(myfolder, str(i) + '_' + file.lower())
        os.rename(current,new)
        i += 1


for i, file in enumerate(files):
    print(i, str(i+1) + '_' + file.lower())