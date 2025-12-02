#!/usr/bin/python3

with open("input_2.txt", "r", encoding="UTF-8") as file:
  for line in file:
    raw_range = line.strip().split(',')
  ranges = []
  for x in raw_range:
    ranges = ranges + [list(map(int, x.split('-')))]
  
  res = 0
  cnt = 0
  for [a,b] in ranges:
    for x in range(a, b+1):
      val = str(x)
      l = len(val)
      if l % 2 == 0:
        if val[0:int(l/2)] == val[int(l/2):]:
          res = res + int(val)
          cnt = cnt + 1
          #print(f'{val}: {res}')
  print(f'{cnt}: {res}')

def chunker(lst, n):
  for i in range(0, len(lst), n):
    yield lst[i:i + n]

with open("input_2.txt", "r", encoding="UTF-8") as file:
  for line in file:
    raw_range = line.strip().split(',')
  ranges = []
  for x in raw_range:
    ranges = ranges + [list(map(int, x.split('-')))]
  
  res = 0
  cnt = 0
  for [a,b] in ranges:
    for x in range(a, b+1):
      val = str(x)
      l = len(val)
      fraud = False
      for pat_len in range(1, int(l/2)+1):
        if l/pat_len == int(l/pat_len):
          pat = val[0:pat_len]
          if all( map(lambda x: pat == x, chunker(val, pat_len)) ):
            fraud = True
            break
      if fraud:
        res = res + int(val)
        cnt = cnt + 1
        #print(f'{val}: {res}')
  print(f'{cnt}: {res}')
