#!/usr/bin/env python
# coding: utf-8

# # This demo app is designed for normal user who wants to predict 
# # or know a class of a value based on data provided

# In[ ]:


from fuu1u import LogReg,Lreg,multi_LogReg,multi_Lreg


print("Welcome to the AI problem solver!\n")
print("please notice that this programme just for numeric data if your data have any strings we recomed you to fix your data first either by dummies or encoder")

data = input("please enter the name of problematic dataset that attached at the same file with this programme\n")
y = input("\n for Regression problem  press: 1 \n for classification problem press: 2\n")
def solver(data,problem_type):
    
    if problem_type=='1':
        z =input("forlinearRegresstion with just one feature press: 1 \n for multi features press : 2\n")
        if z=="1":
            
            info = input("enter the name of the column you want to predict\n")
            value = input("enter the value to be predicted\n")
            Lreg(data,info,value)
    
        else:
            infos = input("enter the name of the column you want to predict\n")
            values = input("enter the number of features to be predicted\n")
            multi_Lreg(data,infos,values)

        
       
        
    else:
        b=input("for binary classification press: 1 \n for multi classification press : 2\n")
        if b=="1":
            
            info = input("enter the name of the column that classification built on\n")
            value = input("enter the value to be classified\n")
            LogReg(data,info,value)
    
        else:
            infos = input("enter the name of the column that classification built on\n")
            values = input("enter the number of features to be classified\n")
            multi_LogReg(data,infos,values)

        
        
        
          
        
        
solver(data,y)      


# In[8]:


from fuu1u import Lreg
Lreg


# In[ ]:




