"""
Converts a CSV to a LaTeX table.

Takes a path and creates an aesthetically, organized table. Currently, it only
supports space breaks.

"""

import csv

print("Enter the csv filepath: ")
filename = input()

reader = csv.reader(open(filename))
csv = []
len_arr = []

for i, row in enumerate(reader):
    csv.append([])
    for j, entry in enumerate(row):
        # determine max length for the column
        if len(len_arr) < j + 1:
            len_arr.append(len(entry))
        elif len(entry) > len_arr[j]:
            len_arr[j] = len(entry)

        csv[i].append(entry)

for row in csv:
    for i, elem in enumerate(row):
        max_len = len_arr[i]
        fluff_len = max_len - len(elem)

        fluff = ""
        for j in range(fluff_len):
            fluff = fluff + " "

        print(elem + fluff, end='')
        if i < len(row) - 1:
            print(end=' & ');
    print(' \\\\')

