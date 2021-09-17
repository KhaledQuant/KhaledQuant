#!/usr/bin/env python

import os
#from tkinter import *
import tkinter as tk
#import pandas as pd

root=tk.Tk()
#rr=Tk() # We will change Tk() to tk.Tk() inside the functions below

"""
dataset=pd.read_csv("ratios.csv", header=0, infer_datetime_format=True, parse_dates=["Num"], index_col=["Num"])

default=dataset["Default"]
default=list(default)
print(default[1])
"""

def sort_series_up(w):
 for i in range(len(w)-1):
  for j in range(len(w)-1):
   if w[j]>=w[j+1]:
    v=w[j]
    w[j]=w[j+1]
    w[j+1]=v
    del v

def min_value(series):
 """This function calculates the min value in a series"""
 y=[]
 for i in range(len(series)):
  y.append(series[i])
 sort_series_up(y)
 x=y[0]
 del y
 return x

def rank_of_min_value(series):
 """This function returns the order min value of a series"""
 y=[]
 ranks=[]
 for i in range(len(series)):
  y.append(series[i])
  ranks.append(i+1)
 for i in range(len(y)-1):
  for j in range(len(y)-1):
   if y[j]>=y[j+1]:
    v=y[j]
    y[j]=y[j+1]
    y[j+1]=v
    rk=ranks[j]
    ranks[j]=ranks[j+1]
    ranks[j+1]=rk
    del v, rk
 x=ranks[0]
 del y, ranks
 return x

def split_value(binary_series, c_series):
 """This function returns the value at which the series will be split"""
 w=[]
 w1=[]
 for i in range(len(c_series)):
  w.append(binary_series[i])
  w1.append(c_series[i])
 for i in range(len(w1)):
  w1[i]=float(w1[i])
 for j in range(len(w1)-1):
  for i in range(len(w1)-1):
   if w1[i]>=w1[i+1]:
    z=w1[i]
    w1[i]=w1[i+1]
    w1[i+1]=z
    z=w[i]
    w[i]=w[i+1]
    w[i+1]=z
    del z
 number_1_inf=[]
 number_1_sup_or_equal=[]
 number_0_inf=[]
 number_0_sup_or_equal=[]
 number_inf=[]
 number_sup_or_equal=[]
 GiNi_1_inf=[]
 GiNi_0_inf=[]
 GiNi_inf=[]
 GiNi_0_sup_or_equal=[]
 GiNi_1_sup_or_equal=[]
 GiNi_sup_or_equal=[]
 GiNi_total=[]
 
 number_inf.append(1)
 for i in range(1,len(c_series)):
  number_inf.append(i)
 
 for i in range(len(c_series)):
  number_sup_or_equal.append(len(c_series)-i)
 
 for i in range(len(c_series)):
  number_1_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1

 for i in range(len(c_series)):
  number_0_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1

 for i in range(len(c_series)):
  number_1_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  number_0_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  GiNi_1_inf.append((number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]))

 for i in range(len(c_series)):
  GiNi_0_inf.append((number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]))
 
 for i in range(len(c_series)):
  GiNi_inf.append(1-(GiNi_1_inf[i]+GiNi_0_inf[i]))

 for i in range(len(c_series)):
  GiNi_1_sup_or_equal.append((number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_0_sup_or_equal.append((number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_sup_or_equal.append(1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_total.append((number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]))
 
 min=min_value(GiNi_total)
 
 rank_min=rank_of_min_value(GiNi_total)
 x=w1[rank_min-1]
 del w, w1, number_1_inf, number_1_sup_or_equal, number_0_inf, number_0_sup_or_equal, number_inf, number_sup_or_equal, GiNi_1_inf, GiNi_0_inf, GiNi_inf, GiNi_0_sup_or_equal, GiNi_1_sup_or_equal, GiNi_sup_or_equal, GiNi_total
 #return w1[rank_min-1]
 return x

def number_inf_to_split_value(binary_series, c_series):
 """Function"""
 w=[]
 w1=[]
 for i in range(len(c_series)):
  w.append(binary_series[i])
  w1.append(c_series[i])
 for i in range(len(w1)):
  w1[i]=float(w1[i])
 for j in range(len(w1)-1):
  for i in range(len(w1)-1):
   if w1[i]>=w1[i+1]:
    z=w1[i]
    w1[i]=w1[i+1]
    w1[i+1]=z
    z=w[i]
    w[i]=w[i+1]
    w[i+1]=z
    del z
 number_1_inf=[]
 number_1_sup_or_equal=[]
 number_0_inf=[]
 number_0_sup_or_equal=[]
 number_inf=[]
 number_sup_or_equal=[]
 GiNi_1_inf=[]
 GiNi_0_inf=[]
 GiNi_inf=[]
 GiNi_0_sup_or_equal=[]
 GiNi_1_sup_or_equal=[]
 GiNi_sup_or_equal=[]
 GiNi_total=[]
 
 number_inf.append(1)
 for i in range(1,len(c_series)):
  number_inf.append(i)
 
 for i in range(len(c_series)):
  number_sup_or_equal.append(len(c_series)-i)
 
 for i in range(len(c_series)):
  number_1_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1

 for i in range(len(c_series)):
  number_0_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1

 for i in range(len(c_series)):
  number_1_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  number_0_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  GiNi_1_inf.append((number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]))

 for i in range(len(c_series)):
  GiNi_0_inf.append((number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]))
 
 for i in range(len(c_series)):
  GiNi_inf.append(1-(GiNi_1_inf[i]+GiNi_0_inf[i]))

 for i in range(len(c_series)):
  GiNi_1_sup_or_equal.append((number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_0_sup_or_equal.append((number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_sup_or_equal.append(1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_total.append((number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]))
 
 
 #return w1[rank_min-1]
 #min=min_value(GiNi_total)
 
 rank_min=rank_of_min_value(GiNi_total)
 x=number_inf[rank_min-1]
 del w, w1, number_1_inf, number_1_sup_or_equal, number_0_inf, number_0_sup_or_equal, number_inf, number_sup_or_equal, GiNi_1_inf, GiNi_0_inf, GiNi_inf, GiNi_0_sup_or_equal, GiNi_1_sup_or_equal, GiNi_sup_or_equal, GiNi_total
 
 return x

def number_sup_to_split_value(binary_series, c_series):
 """Function"""
 w=[]
 w1=[]
 for i in range(len(c_series)):
  w.append(binary_series[i])
  w1.append(c_series[i])
 for i in range(len(w1)):
  w1[i]=float(w1[i])
 for j in range(len(w1)-1):
  for i in range(len(w1)-1):
   if w1[i]>=w1[i+1]:
    z=w1[i]
    w1[i]=w1[i+1]
    w1[i+1]=z
    z=w[i]
    w[i]=w[i+1]
    w[i+1]=z
    del z
 number_1_inf=[]
 number_1_sup_or_equal=[]
 number_0_inf=[]
 number_0_sup_or_equal=[]
 number_inf=[]
 number_sup_or_equal=[]
 GiNi_1_inf=[]
 GiNi_0_inf=[]
 GiNi_inf=[]
 GiNi_0_sup_or_equal=[]
 GiNi_1_sup_or_equal=[]
 GiNi_sup_or_equal=[]
 GiNi_total=[]
 
 number_inf.append(1)
 for i in range(1,len(c_series)):
  number_inf.append(i)
 
 for i in range(len(c_series)):
  number_sup_or_equal.append(len(c_series)-i)
 
 for i in range(len(c_series)):
  number_1_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1

 for i in range(len(c_series)):
  number_0_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1

 for i in range(len(c_series)):
  number_1_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  number_0_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  GiNi_1_inf.append((number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]))

 for i in range(len(c_series)):
  GiNi_0_inf.append((number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]))
 
 for i in range(len(c_series)):
  GiNi_inf.append(1-(GiNi_1_inf[i]+GiNi_0_inf[i]))

 for i in range(len(c_series)):
  GiNi_1_sup_or_equal.append((number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_0_sup_or_equal.append((number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_sup_or_equal.append(1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_total.append((number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]))
 
 #min=min_value(GiNi_total)
 rank_min=rank_of_min_value(GiNi_total)
 x=number_sup_or_equal[rank_min-1]
 del w, w1, number_1_inf, number_1_sup_or_equal, number_0_inf, number_0_sup_or_equal, number_inf, number_sup_or_equal, GiNi_1_inf, GiNi_0_inf, GiNi_inf, GiNi_0_sup_or_equal, GiNi_1_sup_or_equal, GiNi_sup_or_equal, GiNi_total
 return x

def number_1_inf_to_split_value(binary_series, c_series):
 """Function"""
 w=[]
 w1=[]
 for i in range(len(c_series)):
  w.append(binary_series[i])
  w1.append(c_series[i])
 for i in range(len(w1)):
  w1[i]=float(w1[i])
 for j in range(len(w1)-1):
  for i in range(len(w1)-1):
   if w1[i]>=w1[i+1]:
    z=w1[i]
    w1[i]=w1[i+1]
    w1[i+1]=z
    z=w[i]
    w[i]=w[i+1]
    w[i+1]=z
    del z
 number_1_inf=[]
 number_1_sup_or_equal=[]
 number_0_inf=[]
 number_0_sup_or_equal=[]
 number_inf=[]
 number_sup_or_equal=[]
 GiNi_1_inf=[]
 GiNi_0_inf=[]
 GiNi_inf=[]
 GiNi_0_sup_or_equal=[]
 GiNi_1_sup_or_equal=[]
 GiNi_sup_or_equal=[]
 GiNi_total=[]
 
 number_inf.append(1)
 for i in range(1,len(c_series)):
  number_inf.append(i)
 
 for i in range(len(c_series)):
  number_sup_or_equal.append(len(c_series)-i)
 
 for i in range(len(c_series)):
  number_1_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1

 for i in range(len(c_series)):
  number_0_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1

 for i in range(len(c_series)):
  number_1_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  number_0_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  GiNi_1_inf.append((number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]))

 for i in range(len(c_series)):
  GiNi_0_inf.append((number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]))
 
 for i in range(len(c_series)):
  GiNi_inf.append(1-(GiNi_1_inf[i]+GiNi_0_inf[i]))

 for i in range(len(c_series)):
  GiNi_1_sup_or_equal.append((number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_0_sup_or_equal.append((number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_sup_or_equal.append(1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_total.append((number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]))
 
 #min=min_value(GiNi_total)
 rank_min=rank_of_min_value(GiNi_total)
 x=number_1_inf[rank_min-1]
 del w, w1, number_1_inf, number_1_sup_or_equal, number_0_inf, number_0_sup_or_equal, number_inf, number_sup_or_equal, GiNi_1_inf, GiNi_0_inf, GiNi_inf, GiNi_0_sup_or_equal, GiNi_1_sup_or_equal, GiNi_sup_or_equal, GiNi_total
 return x

def number_0_inf_to_split_value(binary_series, c_series):
 """Function"""
 w=[]
 w1=[]
 for i in range(len(c_series)):
  w.append(binary_series[i])
  w1.append(c_series[i])
 for i in range(len(w1)):
  w1[i]=float(w1[i])
 for j in range(len(w1)-1):
  for i in range(len(w1)-1):
   if w1[i]>=w1[i+1]:
    z=w1[i]
    w1[i]=w1[i+1]
    w1[i+1]=z
    z=w[i]
    w[i]=w[i+1]
    w[i+1]=z
    del z
 number_1_inf=[]
 number_1_sup_or_equal=[]
 number_0_inf=[]
 number_0_sup_or_equal=[]
 number_inf=[]
 number_sup_or_equal=[]
 GiNi_1_inf=[]
 GiNi_0_inf=[]
 GiNi_inf=[]
 GiNi_0_sup_or_equal=[]
 GiNi_1_sup_or_equal=[]
 GiNi_sup_or_equal=[]
 GiNi_total=[]
 
 number_inf.append(1)
 for i in range(1,len(c_series)):
  number_inf.append(i)
 
 for i in range(len(c_series)):
  number_sup_or_equal.append(len(c_series)-i)
 
 for i in range(len(c_series)):
  number_1_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1

 for i in range(len(c_series)):
  number_0_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1

 for i in range(len(c_series)):
  number_1_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  number_0_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  GiNi_1_inf.append((number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]))

 for i in range(len(c_series)):
  GiNi_0_inf.append((number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]))
 
 for i in range(len(c_series)):
  GiNi_inf.append(1-(GiNi_1_inf[i]+GiNi_0_inf[i]))

 for i in range(len(c_series)):
  GiNi_1_sup_or_equal.append((number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_0_sup_or_equal.append((number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_sup_or_equal.append(1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_total.append((number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]))
 
 #min=min_value(GiNi_total)
 
 rank_min=rank_of_min_value(GiNi_total)
 x=number_0_inf[rank_min-1]
 del w, w1, number_1_inf, number_1_sup_or_equal, number_0_inf, number_0_sup_or_equal, number_inf, number_sup_or_equal, GiNi_1_inf, GiNi_0_inf, GiNi_inf, GiNi_0_sup_or_equal, GiNi_1_sup_or_equal, GiNi_sup_or_equal, GiNi_total
 return x

def number_1_sup_to_split_value(binary_series, c_series):
 """Function"""
 w=[]
 w1=[]
 for i in range(len(c_series)):
  w.append(binary_series[i])
  w1.append(c_series[i])
 for i in range(len(w1)):
  w1[i]=float(w1[i])
 for j in range(len(w1)-1):
  for i in range(len(w1)-1):
   if w1[i]>=w1[i+1]:
    z=w1[i]
    w1[i]=w1[i+1]
    w1[i+1]=z
    z=w[i]
    w[i]=w[i+1]
    w[i+1]=z
    del z
 number_1_inf=[]
 number_1_sup_or_equal=[]
 number_0_inf=[]
 number_0_sup_or_equal=[]
 number_inf=[]
 number_sup_or_equal=[]
 GiNi_1_inf=[]
 GiNi_0_inf=[]
 GiNi_inf=[]
 GiNi_0_sup_or_equal=[]
 GiNi_1_sup_or_equal=[]
 GiNi_sup_or_equal=[]
 GiNi_total=[]
 
 number_inf.append(1)
 for i in range(1,len(c_series)):
  number_inf.append(i)
 
 for i in range(len(c_series)):
  number_sup_or_equal.append(len(c_series)-i)
 
 for i in range(len(c_series)):
  number_1_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1

 for i in range(len(c_series)):
  number_0_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1

 for i in range(len(c_series)):
  number_1_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  number_0_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  GiNi_1_inf.append((number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]))

 for i in range(len(c_series)):
  GiNi_0_inf.append((number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]))
 
 for i in range(len(c_series)):
  GiNi_inf.append(1-(GiNi_1_inf[i]+GiNi_0_inf[i]))

 for i in range(len(c_series)):
  GiNi_1_sup_or_equal.append((number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_0_sup_or_equal.append((number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_sup_or_equal.append(1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_total.append((number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]))
 
 min=min_value(GiNi_total)
 
 rank_min=rank_of_min_value(GiNi_total)
 
 return number_1_sup_or_equal[rank_min-1]

def number_0_sup_to_split_value(binary_series, c_series):
 """Function"""
 w=[]
 w1=[]
 for i in range(len(c_series)):
  w.append(binary_series[i])
  w1.append(c_series[i])
 for i in range(len(w1)):
  w1[i]=float(w1[i])
 for j in range(len(w1)-1):
  for i in range(len(w1)-1):
   if w1[i]>=w1[i+1]:
    z=w1[i]
    w1[i]=w1[i+1]
    w1[i+1]=z
    z=w[i]
    w[i]=w[i+1]
    w[i+1]=z
    del z
 number_1_inf=[]
 number_1_sup_or_equal=[]
 number_0_inf=[]
 number_0_sup_or_equal=[]
 number_inf=[]
 number_sup_or_equal=[]
 GiNi_1_inf=[]
 GiNi_0_inf=[]
 GiNi_inf=[]
 GiNi_0_sup_or_equal=[]
 GiNi_1_sup_or_equal=[]
 GiNi_sup_or_equal=[]
 GiNi_total=[]
 
 number_inf.append(1)
 for i in range(1,len(c_series)):
  number_inf.append(i)
 
 for i in range(len(c_series)):
  number_sup_or_equal.append(len(c_series)-i)
 
 for i in range(len(c_series)):
  number_1_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1

 for i in range(len(c_series)):
  number_0_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1

 for i in range(len(c_series)):
  number_1_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  number_0_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  GiNi_1_inf.append((number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]))

 for i in range(len(c_series)):
  GiNi_0_inf.append((number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]))
 
 for i in range(len(c_series)):
  GiNi_inf.append(1-(GiNi_1_inf[i]+GiNi_0_inf[i]))

 for i in range(len(c_series)):
  GiNi_1_sup_or_equal.append((number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_0_sup_or_equal.append((number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_sup_or_equal.append(1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_total.append((number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]))
 
 min=min_value(GiNi_total)
 
 rank_min=rank_of_min_value(GiNi_total)
 
 return number_0_sup_or_equal[rank_min-1]

def GiNi_of_split_value(binary_series, c_series):
 """Function"""
 w=[]
 w1=[]
 for i in range(len(c_series)):
  w.append(binary_series[i])
  w1.append(c_series[i])
 for i in range(len(w1)):
  w1[i]=float(w1[i])
 for j in range(len(w1)-1):
  for i in range(len(w1)-1):
   if w1[i]>=w1[i+1]:
    z=w1[i]
    w1[i]=w1[i+1]
    w1[i+1]=z
    z=w[i]
    w[i]=w[i+1]
    w[i+1]=z
    del z
 number_1_inf=[]
 number_1_sup_or_equal=[]
 number_0_inf=[]
 number_0_sup_or_equal=[]
 number_inf=[]
 number_sup_or_equal=[]
 GiNi_1_inf=[]
 GiNi_0_inf=[]
 GiNi_inf=[]
 GiNi_0_sup_or_equal=[]
 GiNi_1_sup_or_equal=[]
 GiNi_sup_or_equal=[]
 GiNi_total=[]
 
 number_inf.append(1)
 for i in range(1,len(c_series)):
  number_inf.append(i)
 
 for i in range(len(c_series)):
  number_sup_or_equal.append(len(c_series)-i)
 
 for i in range(len(c_series)):
  number_1_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1

 for i in range(len(c_series)):
  number_0_inf.append(0)
 
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1

 for i in range(len(c_series)):
  number_1_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  number_0_sup_or_equal.append(0)

 for i in range(len(c_series)):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 for i in range(len(c_series)):
  GiNi_1_inf.append((number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]))

 for i in range(len(c_series)):
  GiNi_0_inf.append((number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]))
 
 for i in range(len(c_series)):
  GiNi_inf.append(1-(GiNi_1_inf[i]+GiNi_0_inf[i]))

 for i in range(len(c_series)):
  GiNi_1_sup_or_equal.append((number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_0_sup_or_equal.append((number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_sup_or_equal.append(1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]))

 for i in range(len(c_series)):
  GiNi_total.append((number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]))
 
 min=min_value(GiNi_total)
 
 rank_min=rank_of_min_value(GiNi_total)
 
 return min

def node(binary_series, c_series):
 """Function"""
 root=Tk()
 #root.configure(background='yellow')
 gg=split_value(binary_series, c_series)
 nb_inf=number_inf_to_split_value(binary_series, c_series)
 nb_sup=number_sup_to_split_value(binary_series, c_series)
 nb_1_inf=number_1_inf_to_split_value(binary_series, c_series)
 nb_0_inf=number_0_inf_to_split_value(binary_series, c_series)
 nb_1_sup=number_1_sup_to_split_value(binary_series, c_series)
 nb_0_sup=number_0_sup_to_split_value(binary_series, c_series)
 prob_inf=nb_1_inf/(nb_1_inf+nb_0_inf)
 prob_sup=nb_1_sup/(nb_1_sup+nb_0_sup)
 g=GiNi_of_split_value(binary_series, c_series)
 d='%'+str(6/10)+'f'
 gg=d%gg
 prob_inf=d%prob_inf
 prob_sup=d%prob_sup
 g=d%g
 root.title("Node")
 Label(root, text="Split value (sv) = "+str(gg)).pack(pady=0)
 Label(root, text="sv rank          = "+str(rank_min)).pack(pady=0)
 Label(root, text="GiNi          = "+str(g)).pack(pady=0)
 Label(root, text="______________________________________").pack(pady=0)
 Label(root, text=".                    < sv  ||   >= sv").pack(pady=0)
 Label(root, text="Binary = 1 :    "+str(nb_1_inf)+"    ||    "+str(nb_1_sup)+"       ").pack(pady=0)
 Label(root, text="Binary = 0 :    "+str(nb_0_inf)+"    ||    "+str(nb_0_sup)+"       ").pack(pady=0)
 Label(root, text="Prob(=1) :    "+str(prob_inf)+"    ||    "+str(prob_sup)+"       ").pack(pady=0)
 root.mainloop()

def G_series_ranked_N(binary_series, ordr, *c_series):
 """Function description"""
 G_values={}
 for i in range(len(c_series)):
  G_values.update({i : (i+1, GiNi_of_split_value(binary_series, c_series[i]))})
 
 for i in range(len(G_values)-1):
  for j in range(len(G_values)-1):
   if G_values[j][1]>=G_values[j+1][1]:
    z=G_values[j+1]
    G_values[j+1]=G_values[j]
    G_values[j]=z
    
 print(G_values[ordr-1][0])


def draw_new_branch(tk_window, right, left):
 """The function does the tree extension with one branch"""

label=tk.Label(text="()------", fg="red", bg="yellow")
label.pack()
btn=tk.Button(text="jhh", state="normal", padx=1, pady=5,  fg="red", bg="yellow")
btn.pack(side="left", padx=30, pady=20)

btn2=tk.Button(text="jhh2", state="normal", padx=1, pady=5, fg="red", bg="yellow")
btn2.pack(side="right", padx=30, pady=20)

btn3=tk.Button(text="jhh3", state="normal", padx=1, pady=5, fg="red", bg="yellow")
#bnt3.grid("""sticky="south""")
#btn3.pack(side="right", padx=30, pady=5)

of=[None]*3
of[0]=tk.Frame(root, borderwidth=0)
of[1]=tk.Frame(root, borderwidth=1)
of[2]=tk.Frame(root, borderwidth=2)

tk.Label(of[0], text="hhh").pack(side="left")
iff=[]
for relief in ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']:
 tk.Button(of[0], text=relief, state="normal", borderwidth=2, relief=relief).pack(side="left")
 #tk.Label(iff[0], text=relief, width=10).pack(side="left")
 #iff[0].pack(side="left", padx=7, pady=5)
 
for relief in ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']:
 tk.Button(of[1], text=relief, state="normal", borderwidth=2, relief=relief).pack(side="left")

for relief in ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']:
 tk.Button(of[2], text="HHHHH", state="normal", borderwidth=2, relief=relief).pack(side="left")

of[0].pack()
of[1].pack(side="left", padx=5, pady=7)
of[2].pack(side="bottom", padx=20, pady=50)
root.mainloop()
os.system("pause")