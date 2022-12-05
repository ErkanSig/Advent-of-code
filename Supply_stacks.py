import re
import pandas as pd

stacks = { 1 : ['D', 'B', 'J', 'V'],
2: ['P', 'V', 'B', 'W', 'R', 'D', 'F'],
3: ['R', 'G', 'F', 'L', 'D', 'C', 'W', 'Q'],
4: ['W', 'J', 'P', 'M', 'L', 'N', 'D', 'B'],
5: ['H', 'N', 'B', 'P', 'C', 'S', 'Q'],
6: ['R', 'D', 'B', 'S', 'N', 'G'],
7: ['Z', 'B', 'P', 'M', 'Q', 'F', 'S', 'H'],
8: ['W', 'L', 'F'],
9: ['S', 'V', 'F', 'M', 'R']}

rearrangements = pd.read_csv('./Data/rearrangement_procedure.txt')

# for row in rearrangements.iterrows():
#     row = re.findall(r'\d+', row[1][0])
#     row[0] = int(row[0])
#     row[1] = int(row[1])
#     row[2] = int(row[2])
#     for move in range(row[0]):
#         stacks[row[2]].append(stacks[row[1]][-1])
#         stacks[row[1]].pop()

# answer = []
# for key, value in stacks.items():
#     print(stacks[key][-1])

# print(stacks[5][len(stacks[5]) - 3:len(stacks[5])])

for row in rearrangements.iterrows():
    row = re.findall(r'\d+', row[1][0])
    row[0] = int(row[0])
    row[1] = int(row[1])
    row[2] = int(row[2])
    for crate in stacks[row[1]][len(stacks[row[1]]) - row[0]:len(stacks[row[1]])]:
        stacks[row[2]].append(crate)
        stacks[row[1]].pop()
    

answer = []
for key, value in stacks.items():
    print(stacks[key][-1])