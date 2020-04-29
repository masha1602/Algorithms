#!/usr/bin/env python
# coding: utf-8

# # ЗАДАНИЕ 2

# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.**
# 

# In[ ]:


import random
import time
import cProfile


# In[318]:


#Решето Эратосфена
def sieve_func(n):     
    sieve = list(range(n*10))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve= set(sieve)
    sieve.remove(0)
    sieve= list(sieve)
    return sieve[n]


# In[313]:


#второй вариант
def prime_num(n):
    prime=list(range(n*10))
    prime[1]=0
    for i in prime: #какие числа надо перебрать
        for j in range(2,n*10): 
            if i%j==0 and i!=j:
                prime[i]=0
    prime= set(prime)
    prime.remove(0)
    prime= list(prime)
    return prime[n]


# In[320]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 sieve_func(10)')
#90.5 µs ± 93.3 µs per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[322]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 sieve_func(100)')
#1.36 ms ± 3.92 ms per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[323]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 sieve_func(1000)')
#10.2 ms ± 8.83 ms per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[321]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 prime_num(10)')
#2.06 ms ± 1.81 ms per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[324]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 prime_num(100)')
#226 ms ± 28.2 ms per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[325]:


get_ipython().run_line_magic('timeit', '-n 1 -r 100 prime_num(1000)')
#25.6 s ± 1.71 s per loop (mean ± std. dev. of 100 runs, 1 loop each)


# In[326]:


cProfile.run('sieve_func(10)')
#  30 function calls in 0.001 seconds


# In[327]:


cProfile.run('sieve_func(100)')
#173 function calls in 0.002 seconds


# In[328]:


cProfile.run('sieve_func(1000)')
#1234 function calls in 0.018 seconds


# In[329]:


cProfile.run('prime_num(10)')
#5 function calls in 0.003 seconds


# In[330]:


cProfile.run('prime_num(100)')
#5 function calls in 0.245 seconds


# In[331]:


cProfile.run('prime_num(1000)')
#5 function calls in 26.500 seconds


# Сложность алгоритмов prime_num и sieve_func O(n)
# Функция, использующая решето Эратосфена, тратит меньше времени на выполнение, но большее количество раз вызывает саму себя.  Учитывая время выполнения алгоритмов, целесообразнее использовать первый.
