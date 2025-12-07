#!/usr/bin/python3

from collections import defaultdict
from copy import copy, deepcopy
from math import gcd

def get_antinodes(a, b):
    r = []

    d0, d1 = a[0]-b[0], a[1]-b[1]
    #print(f'   > {d0} {d1}')
    r.append( [a[0]+d0, a[1]+d1] )
    r.append( [b[0]-d0, b[1]-d1] )

    if d0/3 == float(int(d0/3)) and d1/3 == float(int(d1/3)):
        r.append( [a[0]-int(d0/3), a[1]-int(d0/3)] )
        r.append( [b[0]+int(d0/3), b[1]+int(d0/3)] )

    return r

with open('input_day8.txt', 'r', encoding='UTF-8') as file:
    i = 0
    j = -1
    d = defaultdict(list)
    for line in file:
        l = line.rstrip('\n')
        for j in range(len(l)):
            if l[j] != '.':
                d[l[j]].append((i, j))
        j = len(l)
        i = i + 1
    
    dims = [copy(i), copy(j)]
    
    #print(d)
    antinodes = []
    for k in d.keys():
        #print(f'{k}: {len(d[k])}')
        for i in range(len(d[k])-1):
            for j in range(i+1, len(d[k])):
                #print(f'{d[k][i]}-{d[k][j]}:')
                res = get_antinodes(d[k][i], d[k][j])
                for r in res:
                    #print(f'   {r}')
                    if r[0] >= 0 and r[0] < dims[0] and r[1] >= 0 and r[1] < dims[1]:
                        antinodes.append(r)

    antinodes.sort()
    i = 0
    while i < len(antinodes)-1:
        if antinodes[i] == antinodes[i+1]:
            antinodes.pop(i)
        else:
            i = i + 1

    print(len(antinodes))

def get_antinodes2(a, b):
    r = []

    d0, d1 = a[0]-b[0], a[1]-b[1]
    f = gcd( d0, d1 )
    e0, e1 = int(d0/f), int(d1/f)
    #print(f'   > {d0} {d1}')

    x = [*a]
    
    while x[0] >= 0 and x[0] < 50 and x[1] >= 0 and x[1] < 50:
        x[0], x[1] = x[0]-e0, x[1]-e1
    
    x[0], x[1] = x[0]+e0, x[1]+e1
    while x[0] >= 0 and x[0] < 50 and x[1] >= 0 and x[1] < 50:
        r.append(deepcopy(x))
        x[0], x[1] = x[0]+e0, x[1]+e1

    return r

with open('input_day8.txt', 'r', encoding='UTF-8') as file:
    i = 0
    j = -1
    d = defaultdict(list)
    for line in file:
        l = line.rstrip('\n')
        for j in range(len(l)):
            if l[j] != '.':
                d[l[j]].append((i, j))
        j = len(l)
        i = i + 1
    
    dims = [copy(i), copy(j)]
    
    antinodes = []
    for k in d.keys():
        #print(f'{k}: {len(d[k])}')
        for i in range(len(d[k])-1):
            for j in range(i+1, len(d[k])):
                #print(f'{d[k][i]}-{d[k][j]}:')
                res = get_antinodes2(d[k][i], d[k][j])
                for r in res:
                    #print(f'   {r}')
                    if r[0] >= 0 and r[0] < dims[0] and r[1] >= 0 and r[1] < dims[1]:
                        antinodes.append(r)

    antinodes.sort()
    i = 0
    while i < len(antinodes)-1:
        if antinodes[i] == antinodes[i+1]:
            antinodes.pop(i)
        else:
            i = i + 1

    print(len(antinodes))