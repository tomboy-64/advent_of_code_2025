#!/usr/bin/python

with open("input_day4.txt", "r", encoding="utf-8") as file:
  in_str = []
  for line in file:
    in_str = in_str + [line.strip()]
  
  sum_up = 0
  for ya in range(len(in_str)):
    for xa in range(len(in_str[0])):
      for [dy,dx] in [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]:
        if 0 <= ya + dy*3 and ya + dy*3 < 140 and 0 <= xa + dx*3 and xa + dx*3 < 140:
          if in_str[ya][xa] + in_str[ya+dy][xa+dx] + in_str[ya+dy*2][xa+dx*2] + in_str[ya+dy*3][xa+dx*3] == 'XMAS':
            sum_up = sum_up + 1
  print(sum_up)

with open("input_day4.txt", "r", encoding="utf-8") as file:
  in_str = []
  for line in file:
    in_str = in_str + [line.strip()]
  
  sum_up = 0
  for ya in range(1,len(in_str)-1):
    for xa in range(1,len(in_str[0])-1):
      if in_str[ya][xa] == 'A':
        a = in_str[ya-1][xa-1]
        b = in_str[ya+1][xa+1]
        if (a == 'M' and b == 'S') or (a == 'S' and b == 'M'):
          a = in_str[ya+1][xa-1]
          b = in_str[ya-1][xa+1]
          if (a == 'M' and b == 'S') or (a == 'S' and b == 'M'):
            sum_up = sum_up + 1
  print(sum_up)
