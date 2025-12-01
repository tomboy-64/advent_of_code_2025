#!/usr/bin/python3

with open("input_1.txt", "r", encoding="UTF-8") as file:
    dial = 50
    cnt = 0
    for line in file:
        line = line.strip()

        move = int(line[1:])
        # print(f'{line}')
        if line[0] == "L":
            # print(f'moving {move} to the left')
            dial = dial - move
        elif line[0] == "R":
            # print(f'moving {move} to the right')
            dial = dial + move
        else:
            raise Exception("Bummer, no direction.")

        # print(f'Dial: {dial}')
        while dial < 0:
            dial = 100 + dial
        while dial > 99:
            dial = dial - 100

        if dial == 0:
            cnt = cnt + 1

print(f"Count: {cnt}")


with open("input_1.txt", "r", encoding="UTF-8") as file:
    dial = 50
    cnt = 0
    for line in file:
        line = line.strip()
        move = int(line[1:])

        while move > 0:
            move = move - 1
            if line[0] == "L":
                dial = dial - 1
                #print("<", end="")
                if dial == 0:
                    cnt = cnt + 1
                    #print(".", end="")
                elif dial == -1:
                    dial = 99
            elif line[0] == "R":
                dial = dial + 1
                #print(">", end="")
                if dial == 100:
                    cnt = cnt + 1
                    dial = 0
                    #print(".", end="")
            else:
                raise Exception("Whatcha doin'?")

        #print()
    print(f"Count: {cnt}")
