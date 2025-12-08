#!/usr/bin/python3

from typing import Optional
from copy import deepcopy
from random import randint

def transform1(x):
    if x == 0:
        return [1]
    return None

def transform2(x):
    s = str(x)
    if len(s) % 2 == 0:
        l2 = int(len(s)/2)
        a = int(s[:l2])
        b = int(s[l2:])
        return [a,b]
    return None

def transform3(x):
    return [x*2024]

_lookup = {}

def lookup(x):
    try:
        y = _lookup[x]
    except:
        y = transform1(x)
        if y is None:
            y = transform2(x)
        if y is None:
            y = transform3(x)
        _lookup[x] = y
    return y

_resolve = {}

def resolve(x, cnt):
    try:
        r1 = _resolve[x]
    except:
        _resolve[x] = {}
        r1 = _resolve[x]
    
    try:
        r2 = r1[cnt]
    except:
        if cnt == 0:
            r1[0] = 1
            r2 = 1
        else:
            r2 = 0
            for y in lookup(x):
                r2 += resolve(y, cnt-1)
        #print(f'called resolve({x}, {cnt}): {r2}')
    return r2



with open('input_day11.txt', 'r', encoding='UTF-8') as file:
    arr = []
    for line in file:
        arr1 = list(map(int, line.strip().split()))

    arr = []
    for x in arr1:
        arr.append((x,0))
    print(arr)

    total25 = 0
    for x in arr1:
        y = resolve(x, 50)
        print(f'{x}: {y}')
        total25 += y

        print(f'lookup: {len(_lookup)} resolve: {len(_resolve)}')

    print(total25)
    #print(total75)