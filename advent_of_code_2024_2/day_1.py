#!/usr/bin/python

with open("input_day1.txt", 'r') as file:
    list1 = []
    list2 = []
    for line in file:
        numbers = line.strip().split()

        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

    list1.sort()
    list2.sort()

    difference_count = 0
    for (el1, el2) in zip(list1, list2):
        difference_count = difference_count  + abs(el1 - el2);

    print(difference_count)

with open("input_day1.txt", 'r') as file:
    list1 = []
    list2 = []
    for line in file:
        numbers = line.strip().split()

        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

    list1.sort()
    list2.sort()

    sim_score = 0
    el1_cache = -1
    count_cache = 0
    for el1 in list1:
        if el1 == el1_cache:
            sim_score = sim_score + count_cache
            continue

        while len(list2) > 0 and list2[0] < el1:
            list2.pop(0)
        
        count_cache = 0
        while len(list2) > 0 and el1 == list2[0]:
            count_cache = count_cache + el1
            list2.pop(0)

        sim_score = sim_score + count_cache
        
        el1_cache = el1

    print(sim_score)
