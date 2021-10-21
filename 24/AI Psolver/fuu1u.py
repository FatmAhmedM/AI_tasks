#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import imports
import pandas 
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
def Lreg(data,preColumnName,ToPredictValue):
    
    df = pandas.read_csv(data)
    out = df[preColumnName]
    inpu = df.drop(preColumnName,axis='columns')
    mod = LinearRegression()
    mod.fit(inpu,out)
    pre =mod.predict([[int(ToPredictValue)]])
    print(f'The pridicted value : {pre} ')
    accuracy = mod.score(inpu,out)
    print(f'\n model accuracy : {accuracy}')




def number_Of_inputs(x):
    list =[]
    counter = 1
    for i in range(int(x)):
        colNames = int(input(f'enter your {counter+i} prediction\n'))
        list.append(colNames)
    return list 




def multi_Lreg(data,preColumnName,Number_of_Values):
    list = number_Of_inputs(int(Number_of_Values))
    
    df = pandas.read_csv(data)
    out = df[preColumnName]
    inpu = df.drop(preColumnName,axis='columns')
    mod = LinearRegression()
    mod.fit(inpu,out)
    pre =mod.predict([list])
     
    print(f'The pridicted value : {pre} ')
    accuracy = mod.score(inpu,out)
    print(f'\n model accuracy : {accuracy}')


          
def LogReg(data,preColumnName,ToPredictValue):
    
    df = pandas.read_csv(data)
    out = df[preColumnName]
    inpu = df.drop(preColumnName,axis='columns')
    mod = LogisticRegression()
    mod.fit(inpu,out)
    pre =mod.predict([[int(ToPredictValue)]])
    print(f'The pridicted value : {pre} ')
    accuracy = mod.score(inpu,out)
    print(f'\n model accuracy : {accuracy}')
        

def multi_LogReg(data,preColumnName,Number_of_Values):
    list = number_Of_inputs(int(Number_of_Values))
    

    
    df = pandas.read_csv(data)
    out = df[preColumnName]
    inpu = df.drop(preColumnName,axis='columns')
    mod = LogisticRegression()
    mod.fit(inpu,out)
    pre =mod.predict([list])
    print(f'The pridicted value : {pre} ')
    accuracy = mod.score(inpu,out)
    print(f'\n model accuracy : {accuracy}')

