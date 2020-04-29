#!/usr/bin/env python
# coding: utf-8

# # COLLECTIONS MODULE

# In[1]:


from collections import Counter, namedtuple, deque, defaultdict, OrderedDict, ChainMap
import argparse


# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

# In[9]:


#Задача 1
from collections import namedtuple
from collections import ChainMap
import statistics
below=[]
above=[]
Org_all=ChainMap()
prop= ['Название_предприятия', 'Квартал_1', 'Квартал_2', 'Квартал_3', 'Квартал_4', 'Год' ]
Org= namedtuple('ORG', prop)
n=int(input('Введите число предприятий: '))
for i in range(n):
    name= input('Введите название предприятия: ')
    kv1= int(input('Введите выручку за 1 квартал: '))
    kv2= int(input('Введите выручку за 2 квартал: '))
    kv3= int(input('Введите выручку за 3 квартал: '))
    kv4= int(input('Введите выручку за 4 квартал: '))
    year=kv1+kv2+kv3+kv4
    Firm= Org(name, kv1, kv2, kv3, kv4, year)
    Org_all[i]=Firm
years=[]
for i in range(n):
    years.append(Org_all[i][5])
mean= statistics.mean(years)
for i in range(n):
    if Org_all[i][5]>mean:
        above.append(Org_all[i][0])
    else:
        below.append(Org_all[i][0])
print('Предприятие с выручкой выше среднего: ', above )
print('Предприятие с выручкой ниже среднего: ', below)


# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’]. Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# In[85]:


from collections import deque
import numpy as np
n1= np.array(deque((input('Введите число 1: '))))
n2= np.array(deque((input('Введите число 2: '))))
print("Число 1: " , n1)
print('Число 2: ', n2)
dict1 = {'A': '10' , 'B': '11', 'C': '12', 'D' : '13', 'E': '14', 'F': '15', 
              '1':'1', '2':'2', '3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9', '0': '0'}
dict2 ={'10': 'A' , '11': 'B', '12': 'C', '13' : 'D', '14': 'E', '15': 'F', 
              '1':'1', '2':'2', '3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9', '0': '0'}
num1 = np.array([dict1[x] for x in n1])
num2 = np.array([dict1[x] for x in n2])
num1_10=0
num2_10=0
num1 = [int(i) for i in num1]
st=len(num1)-1
for i in num1:
    num1_10+=i*(16**st)
    st-=1

num2 = [int(i) for i in num2]
st=len(num2)-1
for i in num2:
    num2_10+=i*(16**st)
    st-=1

summa=num1_10+num2_10
summa_16=[]
while summa%16!=0 :
    i=summa%16
    summa_16.append(i)
    summa//=16
summa_16= summa_16[::-1]
summa_16 = [str(i) for i in summa_16]

summa_16 = np.array([dict2[x] for x in summa_16])
print("Сумма чисел: ", summa_16)


proizv=num1_10*num2_10
proizv_16=[]
while proizv%16!=0 :
    i=proizv%16
    proizv_16.append(i)
    proizv//=16
proizv_16= proizv_16[::-1]
proizv_16 = [str(i) for i in proizv_16]

proizv_16 = np.array([dict2[x] for x in proizv_16])
print("Произведение чисел: ", proizv_16)

