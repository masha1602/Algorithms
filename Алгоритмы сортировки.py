#!/usr/bin/env python
# coding: utf-8

# Алгоритмы сортировки

# In[3]:


import random


# # СОРТИРОВКА ПУЗЫРЬКОМ

# In[6]:


n=1
while n< len(array):
    for i in range(len(array)- n):
        if array[i]> array [i+1]:
            array[i], array[i+1]= array[i+1], array[i]
    n+=1
    print(array)


# # СОРТИРОВКА ВЫБОРОМ

# In[24]:


def selection_sort(array):
    for i in range(len(array)): #проходит весь массив
        idx_min=i #при каждой итерации индецс мин обновляется 
        for j in range(i+1, len(array)): #нужно чтобы итерирование начиналось после последнего отфильтрованного элемента
            if array[j] < array[idx_min]: #если итерируемый объект меньше  то заменяем индекс мин на индекс итерируемого а затем и сами элементы через i
                idx_min=j
        
        array[idx_min], array[i]= array[i], array[idx_min]
        print(array)


# In[27]:


selection_sort(array)


# # СОРТИРОВКА ВСТАВКАМИ

# In[30]:


def insertion_sort (array):
    for i in range (1, len(array)): #нулевой индекс не берем так как слева ничего не стоит
        spam=array[i]
        j=i
        while array[j-1] > spam and j>0: 
            array[j] = array[j-1]
            j-=1
        array[j]= spam
        print(array)
                


# # СОРТИРОВКА ШЕЛЛА

# In[41]:


def shell (array):
    assert len(array) < 4000, 'Array is too big for Shell'
    
    def new_increment (array):
        inc= [1,4,10,23,57,132,301,701,1750]
        
        while len(array) <= inc[-1]:
            inc.pop()
        while len(inc)>0:
            yield inc.pop()
    count=0
    for increment in new_increment(array):
        for i in range (increment, len(array)):
            for j in range( i, increment -1 , - increment):
                if array[j-increment] <= array[j]:
                    break
                array[j], array[j-increment]= array[j-increment], array [j]
                count+=1
                print(array) #if array is not large
                print(count)
                
            


# In[42]:


shell(array)


# # СОРТИРОВКА ХОАРА

# In[49]:


def quick(array): #использует доп.память 
    if len(array)<=1: #базовый случай
        return array

    pivot= random.choice(array)
    small=[]
    med=[]
    large=[]
    for item in array:
        if item < pivot :
            small.append(item)
        elif item==pivot:
            med.append(item)
        elif item> pivot:
            large.append(item)
        else: 
            raise Exception('ERROR')
    return quick(small) + med + quick(large)


# In[50]:


new= quick(array)
new


# In[62]:


def quick_no_memory(array, fst, lst): #использует доп.память 
    if fst>=lst: #базовый случай
        return array

    pivot= array[random.randint(fst,lst)]
    i,j=fst,lst
    
    while i<=j:
        while array[i] < pivot:
            i+=1
        while array[j]> pivot:
            j-=1
        
        if i<= j:
            array[i], array[j]= array[j], array[i]
            i,j= i+1, j-1
        quick_no_memory(array, fst, j)
        quick_no_memory(array, i, lst)
        return(array)
   


# In[63]:


quick_no_memory(array, 0, len(array)-1)


# # Встроенная сортировка

# In[64]:


#Create array
array= [i for i in range(10)]
random.shuffle(array)


# In[67]:


def reverse_array(array):
    for i in range(len(array)//2):
        array[i], array[len(array)-i-1] = array[len(array)-i-1], array[i]


# In[74]:


print(array)
array.reverse()
array


# In[75]:


array.sort(reverse=True)
print(array)


# In[77]:


t=tuple(random.randint(0,100) for i in range(10))
t=tuple(sorted(t))


# In[81]:


from collections import namedtuple
from operator import attrgetter
Person= namedtuple('Person', 'name, age')
p1= Person('Lol', 15)
p2=Person('Kek', 45)
p3=Person('Ololo', 125)

people=[p1,p2,p3]

result= sorted(people, key= attrgetter('age'))
result


# In[94]:


size= int(input('Введите размер сортируемого массива: '))
array= [random.randint(-100,100) for i in range(size)]
array


# # СОРТИРОВКА ПУЗЫРЬКОМ Reverse

# In[78]:


import random
size= int(input('Введите размер сортируемого массива'))
array= [random.randint(-100,100) for i in range(size)]
array


# In[81]:


def bubble_sort(array):
    stop = True
    print('Начальный массив', array)
    while stop:
        stop = False
        for i in range( len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                stop = True
    return array


# In[82]:


bubble_sort(array)


# # СОРТИРОВКА СЛИЯНИЕМ

# In[83]:


#Создаем функцию слияния
def merge(A, B):
    Res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            Res.append(A[i]) 
            i += 1 
        else:
            Res.append(B[j]) 
            j += 1 
    Res += A[i:] + B[j:] 
    return Res


# In[89]:


def MergeSort(array): 
    if len(array) <= 1: #частный случай для рекурсии
        return array 
    else:
        L = array[:len(array) // 2] 
        R = array[len(array) // 2:] 
    return merge(MergeSort(L), MergeSort(R))


# In[90]:


MergeSort (array)


# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

# In[ ]:


size= int(input('Введите размер сортируемого массива'))
array= [random.randint(-100,100) for i in range(size)]
if len(array)%2==0:
    array.append(1)


# In[95]:


def quick(array):
    if len(array)<=1: #базовый случай
        return array
    pivot= random.choice(array)
    smaller=[]
    med=[]
    bigger=[]
    for item in array:
        if item < pivot :
            smaller.append(item)
        elif item==pivot:
            med.append(item)
        elif item> pivot:
            bigger.append(item)
        else: 
            raise Exception('ERROR')
    return quick(smaller) + med + quick(bigger)


# In[96]:


quick(array)

