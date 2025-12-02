#!/usr/bin/python

from collections import defaultdict
from bisect import bisect

def default_dict():
  return (set(),set())

with open("input_day5.txt", "r", encoding="utf-8") as file:
  orderings = defaultdict(default_dict)
  updates = []
  first = True
  for line in file:
    l = line.strip()
    if l == '':
      first = False
    elif first:
      a = int(l[0:2])
      b = int(l[3:5])
      orderings[a][1].add(b)
      orderings[b][0].add(a)
      #print(f'[{a}|{b}]:\n  orderings[{a}]:> {orderings[a][1]}\n  orderings[{b}]:< {orderings[b][0]}')
    else:
      updates.append(list(map(int,l.split(','))))
  
  sum_up = 0
  for upd in updates:
    #print(upd)
    correct = True
    for i in range(1, len(upd)):
      for j in range(i):
        correct = upd[j] not in orderings[upd[i]][1]
        if correct:
          correct = upd[i] not in orderings[upd[j]][0]
        if not correct:
          #print(f'upd[{j}]: {upd[j]} ::: upd[{i}]: {upd[i]}')
          break
      if not correct:
        break
    if correct:
      x = upd[int(len(upd) / 2)]
      #print(x)
      sum_up = sum_up + x

  print(sum_up)
  
  sum_up = 0
  for upd in updates:
    correct = True
    i = 1
    while i < len(upd):
      for j in range(i):
        if upd[j] in orderings[upd[i]][1]:
          correct = False
          upd[i], upd[j] = upd[j], upd[i]
          i = 1
          break
        if upd[i] in orderings[upd[j]][0]:
          correct = False
          upd[i], upd[j] = upd[j], upd[i]
          i = 1
          break
      i = i + 1
    if not correct:
      x = upd[int(len(upd) / 2)]
      sum_up = sum_up + x

  print(sum_up)
