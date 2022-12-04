import pandas as pd

pair_assignments = pd.read_csv('./Data/pair_assignments.csv')

fully_contained = 0
for row in pair_assignments.iterrows():
    elf1 = range(int(row[1][0].split('-')[0]), int(row[1][0].split('-')[1]) + 1)
    elf2 = range(int(row[1][1].split('-')[0]), int(row[1][1].split('-')[1]) + 1)
    
    sec_contained = 0
    for sec in elf1:
        if sec in elf2:
            sec_contained +=1
    if sec_contained == len(elf1):
        fully_contained += 1
        continue

    sec_contained = 0
    for sec in elf2:
        if sec in elf1:
            sec_contained +=1
    if sec_contained == len(elf2):
        fully_contained += 1
print(fully_contained)

total_overlap = 0
for row in pair_assignments.iterrows():
    elf1 = range(int(row[1][0].split('-')[0]), int(row[1][0].split('-')[1]) + 1)
    elf2 = range(int(row[1][1].split('-')[0]), int(row[1][1].split('-')[1]) + 1)
    
    overlap = False
    for sec in elf1:
        if sec in elf2:
            total_overlap += 1
            overlap = True
        if overlap:
            break
print(total_overlap)