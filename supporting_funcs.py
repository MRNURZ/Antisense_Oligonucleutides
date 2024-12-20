# -*- coding: utf-8 -*-

"""
Created on Mon Aug 1 10:11 2022

@author: Manal Rahal

The following scripts are collection of useful functions used 
for the pre processing of datasets. 

"""

import pandas as pd

import numpy as np


def get_null_percentage(df):
    
    percent_null = df.isnull().mean() * 100
    
    missing_value_df = pd.DataFrame({'column_name': df.columns,
                                 'percent_missing_values': percent_null})
    
    return missing_value_df

def isinfinitecolumns(df):
    
    ds = df.isin([np.inf, -np.inf]).sum()
    
    print(ds)

    
def isnullcolumns(df):
    
    return df.isnull().sum()


def remove_FLP_PO(df):
    
    compare_df = df[df[Vinj]==25]
    
    #compare strings
    #drop longest
    #Data from the largest load (biggest injection volume) should not be used for picking attributes for the FLP (n), n-1 and n-PO. 
    #Due to the load , tr, width and skewness is not correct. In this cases this data points are wrong, remove them.

    
def find_outliers_IQR(df):
    
    q1=df.quantile(0.25)
    
    q3=df.quantile(0.75)
    
    IQR=q3-q1
    
    outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]
    
    return outliers


def draw_scatter(df1, df2):
    
    fig = px.scatter(x=df1['tR1'], y=df2['tR2'])
    
    fig.show()
    

def return_phosphated_seq(df):
    
    phosphatedvec = []
    
    for i, seq in enumerate (df["Sequence"]):
        
        if seq.count('*') > 0:
            
            phosphatedvec = np.append(phosphatedvec, seq)
    
    return phosphatedvec


def is_phosphated(seq):
        
        if seq.count('*') > 0:
            
            return True
    
        else:
            return False

        
def percentage_phosphated(df):
    
    phosphatedcount = 0
    
    for i, seq in enumerate (df["Sequence"]):
        
        if seq.count('*') > 0:
            
            phosphatedcount = phosphatedcount + 1
    
    return (phosphatedcount/ len(df))*100
        

def is_lost_sulfur(seq):
    return lambda seq: str(seq).contains("-P=O")

def count_sulfur(seq):
    count_sf=0
    count_sf = sequence_1.count('*')
    if "-P=O" in sequence_1:
        count_sf = count_sf - 1
    return count_sf

def generate_ID(df, Gradient):#generate a unique id column to reference shortmers
    generate_ID = []
    i=0
    for i in range(len(df_G)):
        generate_ID.append('_'.join([Gradient, f"{i}"]))
    return generate_ID
