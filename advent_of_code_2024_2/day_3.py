#!/usr/bin/python

from typing import Optional

def check_num(char) -> Optional[int]:
  if char in list(map(str, range(0,10))):
    return int(char)
  return None

with open("input_day3.txt", "r", encoding="utf-8") as file:
  in_str = ''
  for line in file:
    in_str = in_str + line.strip()
  sum_up = 0

  i = 0
  while i < len(in_str):
    if in_str[i:i+4] == 'mul(':
      i = i + 4
      a = 0
      while check_num(in_str[i]) != None:
        x = check_num(in_str[i])
        a = a * 10 + x
        i = i + 1
      if a == 0 or in_str[i] != ',':
        continue
      i = i + 1
      b = 0
      while check_num(in_str[i]) != None:
        x = check_num(in_str[i])
        b = b * 10 + x
        i = i + 1
      if b == 0 or in_str[i] != ')':
        continue
      i = i + 1
      sum_up = a * b + sum_up
      #print(f'{a} * {b}: {sum_up}')
    else:
      i = i + 1
  print(sum_up)

with open("input_day3.txt", "r", encoding="utf-8") as file:
  in_str = ''
  for line in file:
    in_str = in_str + line.strip()
  sum_up = 0

  i = 0
  enabled = True
  while i < len(in_str):
    if enabled:
      if in_str[i:i+7] == 'don\'t()':
        enabled = False
        i = i + 7
        continue
    else:
      if in_str[i:i+4] == 'do()':
        enabled = True
        i = i + 4
      else:
        i = i + 1
        continue

    if in_str[i:i+4] == 'mul(':
      i = i + 4
      a = 0
      while check_num(in_str[i]) != None:
        x = check_num(in_str[i])
        a = a * 10 + x
        i = i + 1
      if a == 0 or in_str[i] != ',':
        continue
      i = i + 1
      b = 0
      while check_num(in_str[i]) != None:
        x = check_num(in_str[i])
        b = b * 10 + x
        i = i + 1
      if b == 0 or in_str[i] != ')':
        continue
      i = i + 1
      sum_up = a * b + sum_up
      #print(f'{a} * {b}: {sum_up}')
    else:
      i = i + 1
  print(sum_up)
