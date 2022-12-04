import pandas as pd

rucksacks_df = pd.read_csv('./Data/items.csv')
first_compartment = []
second_compartment = []
for row in rucksacks_df.iterrows():
    first_compartment.append(row[1][0][0:int(len(row[1][0])/2)])
    second_compartment.append(row[1][0][int(len(row[1][0])/2) : len(row[1][0])])
split_rucksacks_df = pd.DataFrame(columns=['First compartment', 'Second compartment'])
split_rucksacks_df['First compartment'] = first_compartment
split_rucksacks_df['Second compartment'] = second_compartment

priority = {'a':1,
'b':2,
'c':3,
'd':4,
'e':5,
'f':6,
'g':7,
'h':8,
'i':9,
'j':10,
'k':11,
'l':12,
'm':13,
'n':14,
'o':15,
'p':16,
'q':17,
'r':18,
's':19,
't':20,
'u':21,
'v':22,
'w':23,
'x':24,
'y':25,
'z':26,
'A':27,
'B':28,
'C':29,
'D':30,
'E':31,
'F':32,
'G':33,
'H':34,
'I':35,
'J':36,
'K':37,
'L':38,
'M':39,
'N':40,
'O':41,
'P':42,
'Q':43,
'R':44,
'S':45,
'T':46,
'U':47,
'V':48,
'W':49,
'X':50,
'Y':51,
'Z':52}

sum = 0
for row in split_rucksacks_df.iterrows():
    checker_letter = []
    for letter in row[1][0]:
        if (letter in row[1][1]) & (letter not in checker_letter):
            sum += priority[letter]
            checker_letter.append(letter)
print(sum)

sum = 0
for i in range(0, rucksacks_df.shape[0],3):
    checker_letter = []
    print(i)
    for letter in rucksacks_df.iloc[i][0]:
        if (letter in rucksacks_df.iloc[i+1][0]) & (letter in rucksacks_df.iloc[i+2][0]):
            print(letter)
            print(rucksacks_df.iloc[i][0])
            print(rucksacks_df.iloc[i+1][0])
            print(rucksacks_df.iloc[i+2][0])
            sum += priority[letter]
            break
            checker_letter.append(letter)
print(sum)