import pandas as pd
calories = pd.read_csv('./Data/calories.csv', sep = "\s+|\t+|\s+\t+|\t+\s+")
# print(calories.head(20))
calories_list = []
calories_count = 0
calories['Calories'] = calories['Calories'].astype(int)
for item in calories['Calories']:
    if item > 0:
        calories_count += item
    else:
        calories_list.append(calories_count)
        calories_count = 0

calories_list_sorted = sorted(calories_list, reverse=True)
print(calories_list_sorted[:3])
top3_total = calories_list_sorted[0] + calories_list_sorted[1] + calories_list_sorted[2]
print(top3_total)
