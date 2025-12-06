#!/usr/bin/python3

from itertools import product, repeat

def process(operands, operators, target):
    x = operands[0]
    for d, t in zip(operands[1:], operators):
        if t == '+':
            x = x + d
        elif t == '*':
            x = x * d
        elif t == '|':
            x = int(str(x) + str(d))
        else:
            Exception('wtf?')
    if x == target:
        return True
    return False

with open('input_day7.txt', 'r', encoding='UTF-8') as file:
    total = 0
    s = ['+', '*']
    for line in file:
        l = line.strip().split()
        r = int(l[0][:-1])
        elements = list(map(int, l[1:]))

        hit = False
        for operands in product(*repeat(s, len(elements)-1)):
            if process(elements, operands, r):
                hit = True
                break
        
        if hit:
            total = total + r

    print(total)

with open('input_day7.txt', 'r', encoding='UTF-8') as file:
    total = 0
    s = ['+', '*', '|']
    for line in file:
        l = line.strip().split()
        r = int(l[0][:-1])
        elements = list(map(int, l[1:]))

        hit = False
        for operands in product(*repeat(s, len(elements)-1)):
            if process(elements, operands, r):
                hit = True
                break
        
        if hit:
            total = total + r

    print(total)
