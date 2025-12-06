#!/usr/bin/python3

with open("input_6.txt", "r", encoding="UTF-8") as file:
  coll = []
  for line in file:
    l = line.strip().split()
    try:
      k = list(map(int, l))
      coll.append(k)
    except:
      signs = l

  total = 0
  for i in range(len(signs)):
    if signs[i] == '*':
      sub_total = 1
      for j in range(len(coll)):
        sub_total = sub_total * coll[j][i]
    else:
      sub_total = 0
      for j in range(len(coll)):
        sub_total = sub_total + coll[j][i]

    total = total + sub_total
  print(total)

with open("input_6.txt", "r", encoding="UTF-8") as file:
  coll = []
  for line in file:
    coll.append(line.rstrip('\n'))

  t = list(map(list, zip(*coll)))

  op = 'x'
  total = 0
  for l in t:
    if ''.join(l).strip() == '':
      op = 'x'
      total = sub_total + total
      continue
    if op == 'x':
      op = l[-1]
      if op == '*':
        sub_total = 1
      elif op == '+':
        sub_total = 0
    if op == '*':
      sub_total = sub_total * int(''.join(l[:-1]))
    elif op == '+':
      sub_total = sub_total + int(''.join(l[:-1]))

  total = total + sub_total
  print(total)
