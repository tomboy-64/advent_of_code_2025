#!/usr/bin/python3

from itertools import repeat

# s - string to search in
# ch = character to be searched
# returns the positions of all appearances
def find_splitter(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

with open('input_7.txt', 'r', encoding='UTF-8') as file:
    i = 0
    beam_positions = set()
    new_beam_positions = set()
    cnt = 0
    for line in file:
        l = line.strip()
        if i == 0:
            s = l.index('S')
            beam_positions.add(s)
        elif i%2 == 1:
            i = i + 1
            continue
        else:
            splitters = find_splitter(l, '^')
            print('splitters', splitters)
            new_beam_positions.clear()
            for bp in beam_positions:
                try:
                    splitters.index(bp)
                    cnt = cnt + 1
                    new_beam_positions.add(bp-1)
                    new_beam_positions.add(bp+1)
                except:
                    new_beam_positions.add(bp)
            print('bp', beam_positions)
            print('nbp', new_beam_positions)
            
            x = beam_positions
            beam_positions = new_beam_positions
            new_beam_positions = x
        i = i + 1
    
    print(cnt)

with open('input_7.txt', 'r', encoding='UTF-8') as file:
    beam_counts = []
    for i, line in enumerate(file):
        l = line.strip()
        if i == 0:
            beam_counts.append(list(repeat(0, len(l))))
            beam_counts[0][l.index('S')] = 1
        elif i%2 == 0:
            beam_counts.append(list(repeat(0, len(l))))
            for j in range(len(l)):
                if l[j] == '^': # here we have a splitter
                    beam_counts[-1][j-1] = beam_counts[-1][j-1] + beam_counts[-2][j]
                    beam_counts[-1][j+1] = beam_counts[-1][j+1] + beam_counts[-2][j]
                else: #here we don't have a splitter
                    beam_counts[-1][j] = beam_counts[-1][j] + beam_counts[-2][j]
    print(sum(beam_counts[-1]))