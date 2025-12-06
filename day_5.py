#!/usr/bin/python3

with open("input_5.txt", "r", encoding="UTF-8") as file:
    tuples = []
    section = 0
    cnt = 0
    for line in file:
        if line.strip() == '':
            if section == 1:
                exit(0)
            section = 1
            continue
        if section == 0:
            a, b = line.strip().split('-')
            tuples.append((int(a),int(b)))
        else:
            num = int(line.strip())
            for (a, b) in tuples:
                if num >= a and num <= b:
                    cnt = cnt + 1
                    break
    print(cnt)

with open("input_5.txt", "r", encoding="UTF-8") as file:
    tuples = []
    cnt = 0
    for line in file:
        if line.strip() == '':
            break
        lower_1, higher_1 = line.strip().split('-')
        lower_1, higher_1 = int(lower_1), int(higher_1)
        merged_or_inserted = False
        for i, (lower_2, higher_2) in enumerate(tuples):
            if higher_1 < (lower_2 - 1):
                #print("distinct range inserted at the beginning: " + str(lower_1) + ' - ' + str(higher_1))
                # python automatically shifts items to the right
                tuples.insert(i, (lower_1, higher_1))
                merged_or_inserted = True
                break 
            elif  lower_1 > (higher_2 + 1):
                continue
            else:
                #print("tuple to be merged: " + str(lower_1) + ' - ' + str(higher_1))
                #print("tuple to merge with: " + str(lower_2) + ' - ' + str(higher_2))

                # create merged tuple
                new_lower = min(lower_1, lower_2)
                new_higher = max(higher_1, higher_2)

                # it can only join the next tuple or tuples
                j = i + 1
                while j < len(tuples): 
                    next_lower, next_higher = tuples[j]
                    if new_higher >= next_higher:
                        tuples.pop(j)
                    elif new_higher >= next_lower:
                        new_higher = next_higher
                        tuples.pop(j)
                    else:
                        break

                # replace the tuple inside the list
                #print("resulting tuple: " + str(new_lower) + ' - ' + str(new_higher))
                tuples[i] = (new_lower, new_higher)
                merged_or_inserted = True
                break
                
        if merged_or_inserted == False:
            #print("distinct range appended: " + str(lower_1) + ' - ' + str(higher_1))
            tuples.append((lower_1, higher_1))

    whole_size = 0   
    for (lower, higher) in tuples:
        #print('range: ' + str(lower) + ' - ' + str(higher))
        whole_size = whole_size + higher - lower + 1
    
    print(whole_size)
