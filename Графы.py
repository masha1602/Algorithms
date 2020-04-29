#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Алгоритм поиска кратчайшего пути в ширину
def bfs (graph, start, finish):
    parent= [None for _ in range (len(graph))]
    is_visited= [False for _ in range (len(graph))]
    deq=deque([start]) #Создаем очередь и помещаем в начало точку откуда будем двигаться 
    is_visited[start]=True 
    
    while len(deq) > 0:
        current= deq.pop() # из конца очереди извлекаем верншину, эта вершина наша отправная точка 
        if current == finish:
            break
        for i, vertex in enumerate(graph[current]): #запускаем внутр. цикл. Будем просматривать все вершины, которые связаны с текущей
            if vertex ==1 and not is_visited[i]: #если очередная вершина равна 1, тоесть есть связь и можно перейти туда, то
                is_visited[i]=True # отмечаем как посещенную
                parent[i]= current #из какой вершины пришли?
                deq.appendleft(i) #добавляем в начало очереди i вершину
                
    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'
    cost=0 #стоимость пути
    way=deque([finish]) #Значение целевой вершины
    i=finish
    
    while parent[i] != start:
        cost+=1
        way.appendleft(parent[i])
        i=parent[i]
    cost+=1
    way.appendleft(start)
    
    return f'Кратчайший путь {list(way)} длиною в {cost} условных единиц'


# In[ ]:


q=[
    [0,0,1,1,9,0,0,0],
    [0,0,9,4,0,0,5,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0],
]


# In[ ]:


def dik(graph, start):
    lenght=len(graph)
    is_visited= [False]* lenght #посещали или нет 
    cost= [float('inf')] * lenght #пока везде бесконечность
    parent= [-1] * lenght 
    
    cost[start] = 0
    min_cost=0
    
    while min_cost< float('inf') : 
        is_visited[start] = True 
        
        for i, vertex in enumerate(graph[start]): #пройдемся по той строке где хранится старт
            if vertex !=0 and not is_visited[i]:#если значение вершины не равно 0(там есть ребро) и вершину не посещали, то проверяем цену
                if cost[i] > vertex+ cost[start]: #если расстояние до итой вершины больше суммы значения кост в вершине старт и сумма рсстояния от вершины старт до этой вершины
                    cost[i]= vertex + cost[start]
                    parent[i]= start
        
        min_cost= float('inf')
        for i in range(lenght):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost= cost[i]
                start= i
                
    return cost


# In[ ]:


#Улучшенная версия, выводит какие вершины нужно пройти.
def dijkstra(graph, start):
    start2 = start
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parents = [-1] * length
    cost[start] = 0
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parents[i] = start
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
                
    # пройдем список родительских вершин, находя родителя для каждого родителя и тд, пока не дойдем до вершины start или
    # не окажется, что родительской вершины не существует. Если пути нет, то вывод-пустой список, иначе - путь из вершин
    parents[start2] = start2
    ways = []
    for j in range(length):
        i = j
        way = []
        if parents[i] != -1:
            way.append(i)
            while 1:
                parent = parents[i]
                way.append(parent)
                i = parent
                if (i == -1) or (i == start2):
                    break
        way = way[::-1]
        ways.append(way)

    return cost, ways


cost, parents = dijkstra(graph, 0)
print(cost)
print(parents)


# In[ ]:


dijkstra(q,0)


# In[ ]:


#На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
graph=[]
j=0
res=0
n = int(input('Введите число друзей: '))
for x in range(n) :
    graph.append([1]*n)
for row in graph:
    row[j]=0
    j+=1
for row in graph:
    for j in row:
        if row[j]==1:
            res+=1
print(*graph, sep='\n')
print(f'{n} друзей пожали руки {int(res/2)} раз')

