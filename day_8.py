#!/usr/bin/python3

from math import sqrt

def distance(a, b):
    c = [0,0,0]
    c[0] = a[0] - b[0]
    c[1] = a[1] - b[1]
    c[2] = a[2] - b[2]

    return sqrt(c[0] ** 2 + c[1] ** 2 + c[2] ** 2)


with open('input_8.txt', 'r', encoding='UTF-8') as file:
    data = []
    for line in file:
        data.append( tuple(map(int, line.strip().split(','))) )

    pair_list = []
    
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            pair_list.append((data[i], data[j]))
            
    dist_list = []
    for a,b in pair_list:
        d = distance(a,b)
        dist_list.append((d, a, b))
    
    dist_list.sort()
    
    #print(dist_list)

    circuits = [{(x[0],x[1],x[2])} for x in data]

    for i in range(1000):
        tgt1 = dist_list[i][1]
        idx1 = next((i for i, s in enumerate(circuits) if tgt1 in s), None)
        s1 = circuits.pop(idx1)
        tgt2 = dist_list[i][2]
        idx2 = next((i for i, s in enumerate(circuits) if tgt2 in s), None)
        if idx2 is None:
            if tgt2 in s1:
                circuits += [s1]
                continue
            raise Exception("This cannot be!")
        s2 = circuits.pop(idx2)

        circuits += [s1.union(s2)]

    sizes = []
    for c in circuits:
        sizes += [len(c)]
    sizes.sort()

    #print(sizes[-3:])
    print(sizes[-3] * sizes[-2] * sizes[-1])

    while len(circuits) > 1:
        i += 1
        #print(len(circuits), dist_list[i])
        tgt1 = dist_list[i][1]
        idx1 = next((i for i, s in enumerate(circuits) if tgt1 in s), None)
        s1 = circuits.pop(idx1)
        tgt2 = dist_list[i][2]
        idx2 = next((i for i, s in enumerate(circuits) if tgt2 in s), None)
        if idx2 is None:
            if tgt2 in s1:
                circuits += [s1]
                continue
            raise Exception("This cannot be!")
        s2 = circuits.pop(idx2)

        circuits += [s1.union(s2)]

    #print(dist_list[i])
    print(dist_list[i][1][0] * dist_list[i][2][0])
    
    