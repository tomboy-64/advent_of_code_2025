#!/usr/bin/python3

with open("input_4.txt", 'r', encoding='UTF-8') as file:
  rolls = []
  for line in file:
    rolls.append(line.strip())

  mat = []
  for i in range(len(rolls)):
    mat.append([])
    for j in range(len(rolls[0])):
      if rolls[i][j] == '@':
        mat[i].append(1)
      else:
        mat[i].append(0)


  total = 0
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if(mat[i][j] == 1):
        adjacent_sum = 0
        if i == 0 and j == 0:
          adjacent_sum = mat[i][ j + 1] + mat[i+1][j] + mat[i+1][j+1]
        elif i == 0 and j == len(mat[0]) - 1:
          adjacent_sum = mat[i][j-1] + mat[i+1][j-1] + mat[i+1][j]
        elif i == 0:
          adjacent_sum = mat[i][j-1] + mat[i][j+1] + mat[i+1][j-1] + mat[i+1][j] + mat[i+1][j+1]
        elif i == len(mat) - 1 and j == 0:
          adjacent_sum =   mat[i - 1][j] + mat[i-1][j+1] + mat[i][j+1] 
        elif i == len(mat) - 1 and j == len(mat[0]) - 1:
          adjacent_sum =   mat[i-1][j-1] + mat[i - 1][j] + mat[i][j-1] 
        elif i == len(mat) - 1:
          adjacent_sum =  mat[i-1][j-1] + mat[i - 1][j] + mat[i-1][j+1] + mat[i][j-1] + mat[i][j+1] 
        elif j == 0:
          adjacent_sum =  mat[i - 1][j] + mat[i-1][j+1] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1]
        elif j == len(mat[0]) - 1:
          adjacent_sum = mat[i-1][j-1] + mat[i - 1][j]+ mat[i][j-1] +  mat[i+1][j-1] + mat[i+1][j] 

        else:
          adjacent_sum = mat[i-1][j-1] + mat[i - 1][j] + mat[i-1][j+1] + mat[i][j-1] + mat[i][j+1] + mat[i+1][j-1] + mat[i+1][j] + mat[i+1][j+1]
        
        if(adjacent_sum) < 4:
          total = total + 1

print(total)

def remove_roll(mat):
  mod_total = 0
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if(mat[i][j] == 1):
        adjacent_sum = 0
        if i == 0 and j == 0:
          adjacent_sum = mat[i][ j + 1] + mat[i+1][j] + mat[i+1][j+1]
        elif i == 0 and j == len(mat[0]) - 1:
          adjacent_sum =  mat[i][j-1]  + mat[i+1][j-1] + mat[i+1][j]
        elif i == 0:
          adjacent_sum = mat[i][j-1] + mat[i][j+1] + mat[i+1][j-1] + mat[i+1][j] + mat[i+1][j+1]
        elif i == len(mat) - 1 and j == 0:
          adjacent_sum = mat[i - 1][j] + mat[i-1][j+1] + mat[i][j+1] 
        elif i == len(mat) - 1 and j == len(mat[0]) - 1:
          adjacent_sum = mat[i-1][j-1] + mat[i - 1][j] + mat[i][j-1] 
        elif i == len(mat) - 1:
          adjacent_sum = mat[i-1][j-1] + mat[i - 1][j] + mat[i-1][j+1] + mat[i][j-1] + mat[i][j+1] 
        elif j == 0:
          adjacent_sum =  mat[i - 1][j] + mat[i-1][j+1] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1]
        elif j == len(mat[0]) - 1:
          adjacent_sum = mat[i-1][j-1] + mat[i - 1][j]+ mat[i][j-1] +  mat[i+1][j-1] + mat[i+1][j] 
        else:
          adjacent_sum = mat[i-1][j-1] + mat[i - 1][j] + mat[i-1][j+1] + mat[i][j-1] + mat[i][j+1] + mat[i+1][j-1] + mat[i+1][j] + mat[i+1][j+1]
        
        if(adjacent_sum) < 4:
          mod_total = mod_total + 1
          mat[i][j] = 0
  
  return mod_total

with open("input_4.txt", 'r', encoding='UTF-8') as file:
  rolls = []
  for line in file:
    rolls.append(line.strip())

  mat = []
  for i in range(len(rolls)):
    mat.append([])
    for j in range(len(rolls[0])):
      if rolls[i][j] == '@':
        mat[i].append(1)
      else:
        mat[i].append(0)

  total = 0

  while True:
    mod_total = remove_roll(mat)
    if mod_total == 0:
      break
    else:
      total = total + mod_total
          

print(total)

















