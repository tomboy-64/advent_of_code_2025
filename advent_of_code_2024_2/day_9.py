#!/usr/bin/python3

from itertools import repeat
from copy import copy

with open('input_day9.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        l = line.strip()
    data = []
    for id in range(int(len(l)/2) + 1):
        for x in repeat(id, int(l[2*id])):
            data.append(x)
        if 2*id < len(l)-1:
            for x in repeat(-1, int(l[2*id+1])):
                data.append(-1)

    # computing checksum here    
    i = 0
    j = len(data)-1

    while i < j:
        if data[i] != -1:
            i = i + 1
            continue
        elif data[j] == -1:
            j = j - 1
            continue
        else:
            data[i], data[j] = data[j], data[i]
    
    total = 0
    for i, v in enumerate(data):
        if v == -1:
            break
        total = total + i*v
    
    print(total)

with open('input_day9.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        l = line.strip()
    
    data = []
    #print(l)
    for i in range(int(len(l)/2)+1):
        data.append((i, int(l[i*2])))
        if i < int(len(l)/2):
            data.append((-1, int(l[i*2+1])))
    #print(data)

    j = len(l)
    while j > 0:
        j = j-1
        file_id = data[j][0]
        if file_id == -1:
            continue
        file_len = data[j][1]
        for i in range(j):
            if data[i][0] == -1 and data[i][1] >= file_len:
                y = data.pop(j)
                data.insert(j, (-1, copy(y[1])))
                x = data.pop(i)
                data.insert(i, y)
                if x[1] > file_len:
                    data.insert(i+1, (x[0], x[1]-file_len))
                break
        #print(data)

    total = 0
    i = 0
    for id, cnt in data:
        if id == -1:
            i = i + cnt
        else:
            for _ in range(cnt):
                total = total + id * i
                i = i + 1
    
    #print(data)
    print(total)