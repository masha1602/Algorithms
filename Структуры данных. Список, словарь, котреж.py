#!/usr/bin/env python
# coding: utf-8

# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

# In[ ]:


a=5
print (f'{a} = {bin(a)}')
b=6
print (f'{b} = {bin(b)}')
#AND OPERATOR
print (f'{a} and {b} = {a & b} ({bin(a & b)})')
#OR 
print (f'{a} or {b} = {a | b} ({bin(a | b)})')
#XOR
print (f'{a} xor {b} = {a ^ b} ({bin(a ^ b)})')

#SHIFT BIN
print (f'{a}>>2= {a>>2} ({bin(a>>2)}))')
print (f'{a}<<2= {a<<2} ({bin(a<<2)}))')


# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки

# In[ ]:


#point A
x1= float(input())
x2= float(input())
#point B
y1= float(input())
y2= float(input())

if x1==x2:
    print(f'x={x1:.2f}')
else:
    k= (y1 - y2) / (x1 - x2)
    b= y2- k* x2
    print (f'y= {k:.2f} * x + {b:.2f}')


#Определить, является ли год, который ввел пользователь, високосным или не високосным.

# In[ ]:


year= int(input('Введите год: '))
if year%4 != 0:
    print('Обычный год')
elif year%100 == 0 :
    if year%400 == 0:
        print('Високосный год')
    else:
        print('Обычный год')
else:
        print('Високосный год')


#Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# In[ ]:


a= int(input('введите первое число: '))
b= int(input('введите второе число: '))
c= int(input('введите третье число: '))
if b < a < c or c < a < b:
    print('Среднее число:', a)
elif a < b < c or c < b < a:
    print('Среднее число:', b)
else:
    print('Среднее число:', c)


#По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

# In[ ]:


a= int(input('введите сторону А'))
b= int(input('введите сторону В'))
c= int(input('введите сторону С'))
if a+b<c or b+c<a or a+c<b:
    print ('Не сущетсвует такого треугольника')
elif a==b==c:
    print('Равносторонний треугольник')
elif a!=b!=c:
    print ('Разносторонний треугольник')
else:
    print ('Равнобедренный треугольник')


# Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.

# In[ ]:


from random import random
a= int(input('введите минимальное значение для целого числа: '))
aa= int(input('введите максимальное значение для целого числа: '))
b= float(input('введите минимальное значение для вещественного числа: '))
bb= float(input('введите максимальное значение для вещественного числа: '))
c= ord(input('введите минимальное значение для символа: '))
cc= ord(input('введите максимальное значение для символа: '))
A= int(random() * (aa - a + 1)) + a
B= random() * (bb - b) + b
C= int(random() * (cc - c + 1)) + c
print ('Случайное целое число:', A)
print ('Случайное вещественное число:', B)
print ('Случайный символ:', chr(C))


# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# In[ ]:


a= ord(input())
b= ord(input())
a = a - ord('a') + 1
b= b- ord('a') + 1
diff= abs(a-b)
print(f'Разница между позициями а и b- {diff}')
#ord()- возвращает числовое представление символа.
#Чтобы узнать порядковый номер буквы надо отнять 97 , так как алфавит начивается с а, ord('a')= 97


# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

# In[ ]:


import numpy as np
a= np.random.randint(0, 100)
b= int(input("Введите число от 0 до 100: "))
n=1
while a!=b and n<10:
        if a>b :
            print('Введенное число меньше загаданного')
            n+=1
            b= int(input("Введите число от 0 до 100: ")) 
        elif a<b :
            print('Введенное число больше загаданного')
            n+=1
            b= int(input("Введите число от 0 до 100: "))
            break
if a==b:
    print('Число угадано')
else:
    print('Число попыток исчерпано')


# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

# In[ ]:


n=int(input('Введите количество элементов: '))
sum=1
x=1
for i in range(n):
    x=x/-2
    sum+=x
print (f'Сумма {n} элементов ряда= {sum} ' )


# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

# In[ ]:


n=int(input('Введите количество элементов: '))
sum=1
x=1
t=n*(n+1)/2
for i in range(n-1):
    x+=1
    sum+=x
if t==sum:
    print ('Тождество доказано')
else:
    print ('Тождество не доказано')


# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

# In[ ]:


a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
a1=a
b1=b
sum_a=0 #так как в цикле происходит изменение самих переменных, то скопируем их в новые для того, чтобы вывести в конце с:
sum_b=0
if a<=9 :
    sum_a=a
if b<=9 :
    sum_b=b
while a>9: #цикл повторяется пока число не станет однозначным
    d= a%10
    a= a//10
    sum_a+=d
while b>9:
    c= b%10
    b= b//10
    sum_b+=c
if sum_a>sum_b:
    print(f'Число с наибольшей суммой чисел- {a1} ')
else:
    print(f'Число с наибольшей суммой чисел- {b1} ')


# In[ ]:


n = int(input('Введите количество чисел: '))
print('Введите последовательность чисел:')
max = 0
num = 0
for i in range(1, n+1):
    a = int(input(f'{i}) '))
    temp = a
    sum = 0
    while temp > 0:
        sum += temp % 10
        temp //= 10
    if sum > max:
        max, num = sum, a
print(f'Наибольшаяя сумма цифр: {max} - у числа: {num}')


# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

# In[ ]:


while True : #infinity loop
    x=input('Введите знак: ')
    if x==0 :
        break
    if x in ('+', '-', '*','/'):
        a= float(input('Введите первое число: '))
        b= float(input('Введите второе число: '))
        if x=='+':
            print(f'{a}+{b}={a+b}')
        elif x=='-':
            print(f'{a}-{b}={a-b}')
        elif x=='*':
            print(f'{a}*{b}={a*b}')
        elif x=='/':
            if b==0:
                print('Деление на 0 невозможно')
            else:
                print(f'{a}/{b}={a/b}')
    else:
        print('Знак ошибочный, введите заново')


#  Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# In[ ]:


num= int(input(''))
even=0
odd=0
while num>0:
    if num%2==0:
        even+=1
        num//=10
    elif num%10!=0:
        odd+=1
        num//=10
print(f'Количество четных элементов- {even} , количество нечетных элементов {odd}' )


# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

# In[ ]:


num=int(input(''))
res=0
while num>0 :
    res= res*10+num%10
    num=num//10
print(res)
    


# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

# In[ ]:


for i in range(32, 128):
    print (f'\t{i}- {chr(i)})', end= '')
    if i % 10 ==1:
        print()


# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# In[ ]:


num=int(input('Введите количество чисел: '))
digit=int(input('Введите искомую цифру'))
count=0
for i in range (1, num+1):
    m=int(input())
    while m>0 :
        if m% 10 == digit:
            count +=1
        m= m//10
print (f'Было введено {count} цифр {digit}')


# Функция бинарного поиска. Работает только на упорядоченном списке. Найти позицию элемента.

# In[ ]:


def bin_search(array, value):
    left=0
    right=len(array)-1
    pos= len(array)//2
    while array[pos]!= value and right>=left:
        if value > array[pos]:
            left=pos+1
        else:
            right=pos-1
        
        pos= (left+right)//2
    return -1 if left>right else pos


# In[ ]:


import random
a=[random.randint(-10000,1000) for _ in range(100)]
a.sort()


# In[ ]:


bin_search(a, 99)


# Разложить отрицательные и положительные числа по разным массивам

# In[ ]:


array= [random.randint(-100,100) for _ in range (20)]
pos=[]
neg=[]
for item in array:
    if item>0:
        pos.append(item)
    else:
        neg.append(item)
        
print(pos)
print(neg)


# In[ ]:


neg=[item for item in array if item<0]
pos=[item for item in array if item>0]
print(pos)
print(neg)


# Вставка элемента в производное места массива

# In[ ]:


num=int(input('Число для вставки'))
pos= int(input('Позиция'))
array.append(None)
i=len(array)-1
while i > pos :
    array[i], array[i-1]= array[i-1], array [i]
    i-=1
array[pos]= num
print(array)


# In[ ]:


#ALTERNATIVE
array.insert(3, 565656)
array


# MATRIX

# In[ ]:


matrix= [[random.randint(1,10) for _ in range(5)] for _ in range (5)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()


# Посчитать сумму строк и столбцов матрицы

# In[ ]:


#Начнем со строки
#Создаем нулевой столбец
sum_column= [0] * len(matrix[0])
for line in matrix:
    sum_line=0
    
    for i, item in enumerate(line): #item-значение строки, i-номер столбца
        sum_line+=item
        sum_column[i]+=item
        
        print(f'{item:>5}', end='')
    
    print(f'   | {sum_line}')
    
print('-'* (len(matrix))*5)

for s in sum_column:
    print(f'{s:>5}', end='')
    
        


# Обмен значений главной и побочной диагонали матрицы

# In[ ]:


size=3
matrix= [[random.randint(1,10) for _ in range(size)] for _ in range (size)]
for line in matrix:
    for item in line:
        print(f'{item:>5}' , end='')
    print()

print ('-------------')
for i in range (size):
    for j in range (size):
        if i==j: #если на диагонали
            spam= matrix[i][j]
            matrix[i][j]= matrix[i][size-1-j]
            matrix[i][size-1-j]= spam
for line in matrix:
    for item in line:
        print(f'{item:>5}' , end='')
    print()


# In[ ]:


#СЛОВАРИ
k=int(input('Number of interprises: '))
enterprises=[]

for i in range(1, k+1):
    name= input('Enter enterprise name:')
    enterprises[name]= [float(input('Plan: ')), float(input('Fact')) ]
    
    enterprises[name].append(enterprises[name][1]/enterprises[name][0])
    
for key, value in enterprises.items():
    if value[1]>10 and value[2] <1:
        print(f'Enterprises {name} earned {value[1]}, which is {value[2]*100:.2f}%')


# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

# In[9]:


a = [0]*8
for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
            a[j-2] += 1
i = 0
while i < len(a):
    print(f'Чисел кратных {i+2} - {a[i]}')
    i += 1
            
                                
                
    

# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.

# In[ ]:


odd=[]
for i, item in enumerate(array):
    if item%2==0:
        odd.append(i)
print('Индексы четных элементов первого массива: ' , odd)
        


#  В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# In[ ]:


array=[random.randint(-100,100) for _ in range(5)]
max=array[0]
min=array[0]
print(array)
for i in array:
    if i>max:
        max=i
    elif i<min:
        min=i
print(max)
print(min)
max_ind= array.index(max)
min_ind=array.index(min)
array[max_ind]= min
array[min_ind]=max
print(array)


# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

# In[ ]:


array=[random.randint(-100,100) for _ in range(10)]
print(f' Исходный массив : {array}')
neg=[]
max=array[0]
for i in array:
    if i<0:
        neg.append(i)
print(f' Отрицательные числа массива: {neg}')
for i in neg:
    if i > max:
        max=i
print(f' Максимальное отрицательное число: {max} находится на поцизии {array.index(max)}')
    
        


# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

# In[ ]:


array=[random.randint(-100,100) for _ in range(10)]
print(f'Массив: {array}')
num_max=0
num_min=0
sum=0
for i in (array):
    if i>num_max:
        num_max=i
    elif i<num_min:
        num_min=i
print(f'Максимальный элемент: {num_max}')
print(f'Минимальный элемент: {num_min}')
if array.index(num_max) > array.index(num_min):
    for i in array[(array.index(num_min)+1) : (array.index(num_max))]:
        sum+=i
else:
    for i in array[(array.index(num_max)+1) : (array.index(num_min))]:
        sum+=i
if sum==0:
    print('Между числами нет элементов')
else:
    print(sum)


# Определить, какое число в массиве встречается чаще всего.

# In[ ]:


array=[random.randint(-100,100) for _ in range(1000)]
max_freq=1
for i in range(len(array)-1):
    freq = 1
    for j in range(i+1,len(array)):
        if array[i] == array[j]:
            freq += 1
    if freq > max_freq:
        max_freq = freq
        num = array[i]

if max_freq > 1:
    print(max_freq, 'раз встречается число: ', num)
else:
    print('Все элементы уникальны')
        


# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

# In[ ]:


m=5
n=4
colsum=0
matrix=[]
for j in range(n):
    row=[]
    s=0
    for i in range (m-1):
        b= int(input(f'Введите элемент {i+1} колонки {j+1} строки: '))
        s+=b
        row.append(b)
    row.append(s)
    matrix.append(row)

for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()

        


# In[ ]:


#Найти максимальный элемент среди минимальных элементов столбцов матрицы.


# In[ ]:


import random
M = int(input('Введите количество столбцов: '))
N = int(input('Введите количество строк: '))
mn= int(input('Введите нижнюю границу для генерации матрицы: '))
mx=int(input('Введите верхнюю границу для генерации матрицы: '))
matrix= [[random.randint(mn, mx) for _ in range (M)] for _ in range (N)]

for line in matrix:
    for item in line:
        print(f'{item:>5}' , end='')
    print()

max_a = matrix[0][0]
for j in range(M):
    min=matrix[0][j]
    for i in range(N):
        if matrix[i][j] < min_a:
            min_a = matrix[i][j]
    if min_a > max_a:
        max_a = min_a
print("Максимальный элемент среди минимальных: ",  max_a)


# In[ ]:


