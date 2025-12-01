#!/usr/bin/python

# strictly increasing or decreasing by 1-3 safe
# increasing or decreasing by 4 and higher unsafe

with open("input_day2.txt", "r", encoding="utf-8") as file:
    safe_reports = 0

    for report in file:
        array = list(map(int, report.strip().split()))

        if array[0] == array[1]:
            continue
        if array[0] > array[1]:
            direction = 1
        else:
            direction = -1

        success = True
        for i in range(len(array) - 1):
            diff = array[i] - array[i + 1]
            if (
                diff != direction * 1
                and diff != direction * 2
                and diff != direction * 3
            ):
                success = False
                break

        if success:
            safe_reports = safe_reports + 1

    print(safe_reports)


with open("input_day2.txt", "r", encoding="UTF-8") as file:
    safe_reports = 0

    for report in file:
        array = list(map(int, report.strip().split()))
        print(f"          {array}")

        i = 0
        bad_level_tolerated = False

        if array[0] == array[1]:
            if array[1] == array[2]:
                continue
            else:
                bad_level_tolerated = True
                array.pop(0)

        if array[0] > array[1]:
            direction = 1
        else:
            direction = -1

        success = True
        while i < len(array) - 1:
            diff = array[i] - array[i + 1]
            if (
                diff != direction * 1
                and diff != direction * 2
                and diff != direction * 3
            ):
                if not bad_level_tolerated:
                    bad_level_tolerated = True
                    array.pop(i+1)
                    continue
                else:
                    success = False
                    break
            i = i + 1


        if success:
            safe_reports = safe_reports + 1
            print(f"safe:     {array}")
        else:
            print(f"not safe: {array}")


    print(safe_reports)
