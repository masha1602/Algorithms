#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import 
import random


# In[ ]:


def insert_1 (array , num=10000, pos= 10):
    array.append(None)
    i=len(array)-1
    while i > pos :
        array[i], array[i-1]= array[i-1], array [i]
        i-=1
    array[pos]= num


# In[ ]:


def insert_2 (array, num=10000, pos= 10):
    array.insert(pos, num)


# In[ ]:


def insert_3 (array, num=10000, pos= 10):
    if array[pos]==num:
        return array
    array.append(None)
    i=1
    while i < pos :
        array[i-1], array[i]= array[i], array [i+1]
        i+=1
    array[pos]= num


# Оценка алгоритмов 

# Замеряем время работы первого алгоритма,  длина входного массива- 50,100,1000

# In[ ]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 insert_1(array=[random.randint(0,100) for _ in range (50)])')
#835 µs ± 1.55 ms per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[ ]:


cProfile.run('insert_1(array=[random.randint(0,100) for _ in range (50)])')
#308 function calls in 0.001 seconds


# In[ ]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 insert_1(array=[random.randint(0,100) for _ in range (100)])')
#1.64 ms ± 1.51 ms per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[ ]:


cProfile.run('insert_1(array=[random.randint(0,100) for _ in range (100)])')
#562 function calls in 0.001 seconds


# In[ ]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 insert_1(array=[random.randint(0,100) for _ in range (1000)])')
#8.6 ms ± 3.7 ms per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[ ]:


cProfile.run('insert_1(array=[random.randint(0,100) for _ in range (1000)])')
#5325 function calls in 0.013 seconds


# Замеряем время работы второго алгоритма,  длина входного массива- 50,100,1000

# In[ ]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 insert_2(array=[random.randint(0,100) for _ in range (50)])')
#338 µs ± 763 µs per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[ ]:


cProfile.run('insert_2(array=[random.randint(0,100) for _ in range (50)])')
# 267 function calls in 0.001 seconds


# In[ ]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 insert_2(array=[random.randint(0,100) for _ in range (100)])')
#701 µs ± 963 µs per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[ ]:


cProfile.run('insert_2(array=[random.randint(0,100) for _ in range (100)])')
# 535 function calls in 0.001 seconds


# In[ ]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 insert_2(array=[random.randint(0,100) for _ in range (1000)])')
#8.78 ms ± 8.13 ms per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[ ]:


cProfile.run('insert_2(array=[random.randint(0,100) for _ in range (1000)])')
#5287 function calls in 0.011 seconds


# Замеряем время работы третьего алгоритма,  длина входного массива- 50,100,1000

# In[ ]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 insert_3(array=[random.randint(0,100) for _ in range (50)])')
#266 µs ± 305 µs per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[ ]:


cProfile.run('insert_3(array=[random.randint(0,100) for _ in range (50)])')
#264 function calls in 0.001 seconds


# In[ ]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 insert_3(array=[random.randint(0,100) for _ in range (100)])')
#567 µs ± 548 µs per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[ ]:


cProfile.run('insert_3(array=[random.randint(0,100) for _ in range (100)])')
#  525 function calls in 0.001 seconds


# In[ ]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 insert_3(array=[random.randint(0,100) for _ in range (1000)])')
#6.3 ms ± 3.71 ms per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[ ]:


cProfile.run('insert_3(array=[random.randint(0,100) for _ in range (1000)])')
# 5290 function calls in 0.007 seconds


# Первая функция при любом размере массива вызывает себя большее количество раз и занимает больше времени на выполнение. Она начинает поиск подходящего индекса с послденего индекса массива, учитывая, что алгоритм должен вставить число на 10 позицию, а длины массивов- 50, 100 и 1000, то уходит много времени на поиск.
# Вторая функция используют встроенную функцию insert.
# Третий алгоритм похож на 1, но начинает поиск с 1 элемента массива. Он имеет лучшие значения по времени и вызывает себя меньшее количество раз. 
# Сложность алгоритмов O(n)
