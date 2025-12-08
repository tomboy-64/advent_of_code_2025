#!/usr/bin/python3

from collections import defaultdict

with open('input_day10.txt', 'r', encoding='UTF-8') as file:
    input_map = []
    for line in file:
        input_map.append(list(map(int, line.strip())))
    
    total = 0
    visited = set()
    left = set()
    for i, line in enumerate(input_map):
        for j, x in enumerate(line):
            if x == 0:
                #print(f'Found 0: ({i},{j}) - ', end='')
                visited.clear()
                left.clear()
                left.add((i,j))
                while len(left) != 0:
                    point = left.pop()
                    visited.add(point)
                    height = input_map[point[0]][point[1]]
                    if height == 9:
                        total = total + 1
                        #print('.', end='')
                        continue
                    if point[0] > 0:
                        new_point = (point[0]-1, point[1])
                        if input_map[new_point[0]][new_point[1]] == height + 1:
                            if new_point not in visited:
                                left.add(new_point)
                    if point[1] > 0:
                        new_point = (point[0], point[1]-1)
                        if input_map[new_point[0]][new_point[1]] == height + 1:
                            if new_point not in visited:
                                left.add(new_point)                        
                    if point[0] < len(input_map)-1:
                        new_point = (point[0]+1, point[1])
                        if input_map[new_point[0]][new_point[1]] == height + 1:
                            if new_point not in visited:
                                left.add(new_point)
                    if point[1] < len(input_map[0])-1:
                        new_point = (point[0], point[1]+1)
                        if input_map[new_point[0]][new_point[1]] == height + 1:
                            if new_point not in visited:
                                left.add(new_point)                        
                #print()

    print(total)

with open('input_day10.txt', 'r', encoding='UTF-8') as file:
    paths = {
        0: defaultdict(int)
    }

    input_map = []
    for i, line in enumerate(file):
        input_map.append(list(map(int, line.strip())))
        for j, x in enumerate(input_map[-1]):
            if x == 0:
                paths[0][(i,j)] = 1

    queue = []
    for i in range(9):
        z = defaultdict(int)
        for y,x in paths[i].keys():
            queue.clear()
            if y > 0:
                queue.append((y-1,x))
            if y < len(input_map)-1:
                queue.append((y+1,x))
            if x > 0:
                queue.append((y,x-1))
            if x < len(input_map[0])-1:
                queue.append((y,x+1))

            cnt = paths[i][(y,x)]
            while len(queue) > 0:
                next_coords = queue.pop(-1)
                if input_map[next_coords[0]][next_coords[1]] == i+1:
                    z[next_coords] += cnt

        paths[i+1] = z
    
    total = 0
    for k in paths[9].keys():
        total += paths[9][k]

    print(total)
