# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 00:00:39 2017

@author: Muddassar Sharif
"""

import numpy as np
import pandas as pd
from sklearn import preprocessing
import pickle
from datetime import datetime
import math
from sklearn.cross_validation import train_test_split
import random as rd
#from multiple_files import *

class graph():

    def __init__(self):
        self.variables= None
        self.key= None
        self.key_for_file=None
        self.df=None
        self.per_y= None
        self.plot= None
        
    def key_from_user(self, key_given):
        self.variables= key_given[0]
        self.key=key_given[1]
        
    def user_input(self, i):  # assuming that the imput is given in tghe form of an array
        self.key_for_file=i
        self.make_dataframe()
    
    def make_dataframe(self):
        
        time={}
        for key in self.key_for_file.keys():
            if "dayyy" in key:
                time[key]= self.key_for_file[key]
                day=self.key_for_file[key]
            if "monthhh" in key:
                time[key]= self.key_for_file[key]
                month=self.key_for_file[key]
            if "yearrr" in key:
                time[key]= self.key_for_file[key]
                year=self.key_for_file[key]
                

        month_key={1:31, 2:28, 3:31, 4:30, 5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        m_array=[]
        d_array=[]
        y_array=[]

        if month[0] < month[1]:
            for m in range(month[0], month[1]+1):
                if m== month[0]:       
                    for d in range(day[0], month_key[m]+1):
                        d_array.append(d)
                        m_array.append(m)
                        y_array.append(year[0])
                elif m== month[1]:       
                    for d in range(1, day[1]+1):
                        d_array.append(d)
                        m_array.append(m)
                        y_array.append(year[0])
                else:
                    for d in range(1, month_key[m]+1):
                        d_array.append(d)
                        m_array.append(m)
                        y_array.append(year[0])
                        
        elif month[0] == month[1]:
                 
            for d in range(day[0], day[1]+1):
                d_array.append(d)
                m_array.append(month[0])
                y_array.append(year[0])
        
        else:
            for m in range(month[0], 13):
                if m== month[0]:       
                    for d in range(day[0], month_key[m]+1):
                        d_array.append(d)
                        m_array.append(m)
                        y_array.append(year[0])
                else:      
                    
                    for d in range(1, month_key[m]+1):
                        d_array.append(d)
                        m_array.append(m)
                        y_array.append(year[0])
            for m in range(1, month[1]+1):
                if m== month[1]:       
                    for d in range(1, day[1]+1):
                        d_array.append(d)
                        m_array.append(m)
                        y_array.append(year[1])
                else:      
                    
                    for d in range(1, month_key[m]+1):
                        d_array.append(d)
                        m_array.append(m)
                        y_array.append(year[1])
                        
         
        number= len(d_array)
        # make empty dataframes
        self.df= pd.DataFrame(columns= self.variables)
        self.plot= pd.DataFrame(columns=[])
        for key in self.variables:          #self.key_for_file.keys():   # replace with the array of selected variables
            print(key)
            if "dayyy" in key:
                self.df[key]=np.array(d_array)
                self.plot["dayyy"]= np.array(d_array)
            elif "monthhh" in key:
                self.df[key]=np.array(m_array)  
                self.plot["monthhh"]= np.array(m_array)
            elif "yearrr" in key:
                self.df[key]=np.array(y_array)
                self.plot["yearrr"]= np.array(y_array)
            
            else:
                print("this is the number")
                print(self.key_for_file[key])
                self.df[key]=np.array([ self.key_for_file[key][0] for i in range(number)])
                
        self.categorical_to_nominal()
    
    
    def categorical_to_nominal(self):
        # copythe code from preporcess.py
        # self.df       self.key   self.variables

        for x in self.variables:

            if ("int" in str(type(np.array(self.df[x])[1]))) or ("float" in str(type(np.array(self.df[x])[1]))) or ("long" in str(type(np.array(self.df[x])[1]))):

                pass
            else:
                print(x)
                self.df[[x]]=self.nom_convert_int(self.df[[x]],x)
              
        return "categoricol to nominal done!" 
    
    def nom_convert_int(self,df,x):
        import numpy as np
        x_c= np.array(df)
        dic=self.key[x]
        c=0
        print(len(x_c))
        for j in range(len(x_c)):
#            print(c)
#            c=c+1
            x_c[j][0]=dic[x_c[j][0]]
        
        return x_c    
 
    
    def get_df_for_per(self):
        # take care of all the conversions here
        return self.df
    
    def set_per_y(self, y):
        self.per_y=y
        self.plot["y"]= np.array(self.per_y)
    
    def get_plot_data(self):
        
        return self.plot
    
    
    def get_key(self):
        return self.key
        
    