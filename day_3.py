#!/usr/bin/python3

with open("input_3.txt", "r", encoding="UTF-8") as file:
  sum_up = 0
  cnt = 0
  for line in file:
    l = line.strip()
    v = [int(l[0]), 0]
    i = 1
    while v[0] < 9 and i < len(l)-1:
      z = int(l[i])
      if z > v[0]:
        v = [z, i]
      i = i + 1
    w = [int(l[v[1]+1]), v[1]+1]
    i = v[1]+2
    while w[0] < 9 and i < len(l):
      z = int(l[i])
      if z > w[0]:
        w = [z, i]
      i = i + 1

    sum_up = sum_up + v[0]*10 + w[0]
  print(sum_up)

with open("input_3.txt", "r", encoding="UTF-8") as file:
  sum_up = 0
  cnt = 0
  for line in file:
    l = list(map(int, line.strip()))
    v = 0
    last_idx = 0
    for i in map(lambda x: len(l) - x, reversed(range(12))):
      #print(f'{last_idx}:{i} ', end='')

      x = max(l[last_idx:i])
      last_idx = l[last_idx:i].index(x) + last_idx + 1
      v = v * 10
      v = v + x
    #print(f'{last_idx}:{i} | ', end='')
    #print(v)
    #print(line, '\n')
    sum_up = sum_up + v
  
  print(sum_up)













