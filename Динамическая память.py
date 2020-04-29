#!/usr/bin/env python
# coding: utf-8

# # Работа с динамической памятью 

# In[3]:


import sys
import random
print(sys.version, sys.platform)
import struct
import ctypes


# Разложить отрицательные и положительные числа по разным массивам. Замерить память локальных объектов. 

# In[186]:


def pos_neg (array= [random.randint(-100,100) for _ in range (50)]):
    pos= set()
    neg= set()
    for item in array:
        if item>0:
            pos.add(item)
        else:
            neg.add(item)
    sum=0
    for obj in locals():
        sum+=sys.getsizeof(obj)
    print(f' Локальные объекты функции: {locals()}')
    print(f'Объкты внутри функции занимают {sum} байт памяти')


# In[187]:


pos_neg()


# In[182]:


def pos_neg3 (array= [random.randint(-100,100) for _ in range (50)]):
    neg= tuple([item for item in array if item<0])
    pos= tuple([item for item in array if item>0]) 
    sum=0
    for obj in locals():
        sum+=sys.getsizeof(obj)
    print(f' Локальные объекты функции: {locals()}')
    print(f'Объкты внутри функции занимают {sum} байт памяти')


# In[183]:


pos_neg3()


# In[184]:


def pos_neg2 (array= [random.randint(-100,100) for _ in range (50)]):
    neg= [item for item in array if item<0]
    pos= [item for item in array if item>0]
    sum=0
    for obj in locals():
        sum+=sys.getsizeof(obj)
    print(f' Локальные объекты функции: {locals()}')
    print(f'Объкты внутри функции занимают {sum} байт памяти')   


# In[185]:


pos_neg2()

