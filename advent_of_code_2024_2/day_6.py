#!/usr/bin/python

import copy

candidates = set()

with open("input_day6.txt", "r", encoding="utf-8") as file:
  maze = []
  guard = (-1,-1)
  y = -1
  for line in file:
    x = line.find('^')
    l = list(line.strip())
    maze.append(l)
    y = y + 1
    if x >= 0:
      guard = [y,x]
      print(f'guard: {guard}')

  dim = [len(maze), len(maze[0])]
  g_dir = '^'
  
  while True:
    maze[guard[0]][guard[1]] = 'X'
    candidates.add([guard[0],guard[1]])
    candidates.add([guard[0]+1,guard[1]])
    candidates.add([guard[0]-1,guard[1]])
    candidates.add([guard[0],guard[1]+1])
    candidates.add([guard[0],guard[1]-1])
    if g_dir == '^':
      # still in area
      if guard[0] > 0:
        # turn right
        if maze[guard[0]-1][guard[1]] == '#':
          g_dir = '>'
        else: # or go ahead
          guard[0] = guard[0] - 1
      elif guard[0] <= 0: # not in area
        break
      else:
        raise Exception("Can't happen. Handled already.")
    elif g_dir == '>':
      # still in area
      if guard[1] < dim[1]-1:
        # turn right
        if maze[guard[0]][guard[1]+1] == '#':
          g_dir = 'v'
        else: # go ahead
          guard[1] = guard[1] + 1
      elif guard[1] >= dim[1]-1: # not in area
        break
      else:
        raise Exception("Can't happen. Handled already. (2)")
    elif g_dir == 'v':
      # still in area
      if guard[0] < dim[0]-1:
        # turn right
        if maze[guard[0]+1][guard[1]] == '#':
          g_dir = '<'
        else: # go ahead
          guard[0] = guard[0] + 1
      elif guard[0] >= dim[0]-1: # not in area
        break
      else:
        raise Exception("Can't happen. Handled already. (3)")
    elif g_dir == '<':
      # still in area
      if guard[1] > 0:
        # turn right
        if maze[guard[0]][guard[1]-1] == '#':
          g_dir = '^'
        else: # go ahead
          guard[1] = guard[1] - 1
      elif guard[1] <= 0: # not in area
        break
      else:
        raise Exception("Can't happen. Handled already. (4)")
    else:
      break

  sum_up = 0
  for line in maze:
    sum_up = sum_up + line.count('X')
  print(sum_up)



def walk(maze, guard):
  turns = []
  g_dir = '^'

  while True:
    maze[guard[0]][guard[1]] = 'X'
    if g_dir == '^':
      # still in area
      if guard[0] > 0:
        # turn right
        if maze[guard[0]-1][guard[1]] == '#':
          if (guard,'>') in turns:
            return True
          turns.append((deepcopy(guard), '>'))
          g_dir = '>'
        else: # or go ahead
          guard[0] = guard[0] - 1
      elif guard[0] <= 0: # not in area
        break
      else:
        raise Exception("Can't happen. Handled already.")
    elif g_dir == '>':
      # still in area
      if guard[1] < dim[1]-1:
        # turn right
        if maze[guard[0]][guard[1]+1] == '#':
          if (guard,'v') in turns:
            return True
          turns.append((deepcopy(guard), 'v'))
          g_dir = 'v'
        else: # go ahead
          guard[1] = guard[1] + 1
      elif guard[1] >= dim[1]-1: # not in area
        break
      else:
        raise Exception("Can't happen. Handled already. (2)")
    elif g_dir == 'v':
      # still in area
      if guard[0] < dim[0]-1:
        # turn right
        if maze[guard[0]+1][guard[1]] == '#':
          if (guard,'<') in turns:
            return True
          turns.append((deepcopy(guard), '<'))          
          g_dir = '<'
        else: # go ahead
          guard[0] = guard[0] + 1
      elif guard[0] >= dim[0]-1: # not in area
        break
      else:
        raise Exception("Can't happen. Handled already. (3)")
    elif g_dir == '<':
      # still in area
      if guard[1] > 0:
        # turn right
        if maze[guard[0]][guard[1]-1] == '#':
          if (guard,'^') in turns:
            return True
          turns.append((deepcopy(guard), '^'))
          g_dir = '^'
        else: # go ahead
          guard[1] = guard[1] - 1
      elif guard[1] <= 0: # not in area
        break
      else:
        raise Exception("Can't happen. Handled already. (4)")
    else:
      break

  return False

with open("input_day6.txt", "r", encoding="utf-8") as file:
  maze = []
  guard = (-1,-1)
  y = -1
  for line in file:
    x = line.find('^')
    l = list(line.strip())
    maze.append(l)
    y = y + 1
    if x >= 0:
      guard = [y,x]
      print(f'guard: {guard}')

  loops = 0
  #print(maze)
  while True:
    try:
      x = candidates.pop()
      m2 = deepcopy(maze)
      m2[x[0]][x[1]] = '#'
      if walk(m2, deepcopy(guard)):
        loops = loops + 1
        #print(loops, f'found for {x} - {len(candidates)} left')
      #else:
      #  print(f'no loop found for {x}')
    except:
      break
  print(loops)
