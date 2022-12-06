import numpy as np
data_stream = open('./Data/Data_stream.txt')
data_stream = data_stream.read()

rolling4 = []
i = 0 
for letter in data_stream:
    i += 1
    rolling4.append(letter)

    if len(rolling4) == 5:
        rolling4.pop(0)
    if len(np.unique(rolling4)) == 4:
        break

print(i)
print(rolling4)

rolling14 = []
i = 0 
for letter in data_stream:
    i += 1
    rolling14.append(letter)

    if len(rolling14) == 15:
        rolling14.pop(0)
    if len(np.unique(rolling14)) == 14:
        break
    
print(i)
print(rolling14)