import pandas as pd

RPS_df = pd.read_csv('./Data/RPS_Strat.csv')

score = 0

for i in range(RPS_df.shape[0]):
    if(RPS_df.iloc[i,0][0] == 'A'):
        if(RPS_df.iloc[i,0][2] == 'X'):
            score += 4 # 1 + 3
        if(RPS_df.iloc[i,0][2] == 'Y'):
            score += 8
        if(RPS_df.iloc[i,0][2] == 'Z'):
            score += 3
    if(RPS_df.iloc[i,0][0] == 'B'):
        if(RPS_df.iloc[i,0][2] == 'X'):
            score += 1
        if(RPS_df.iloc[i,0][2] == 'Y'):
            score += 5
        if(RPS_df.iloc[i,0][2] == 'Z'):
            score += 9
    if(RPS_df.iloc[i,0][0] == 'C'):
        if(RPS_df.iloc[i,0][2] == 'X'):
            score += 7
        if(RPS_df.iloc[i,0][2] == 'Y'):
            score += 2
        if(RPS_df.iloc[i,0][2] == 'Z'):
            score += 6
print(score)

score = 0
for i in range(RPS_df.shape[0]):
    if(RPS_df.iloc[i,0][0] == 'A'):
        if(RPS_df.iloc[i,0][2] == 'X'):
            score += 3 # 3 + 0 
        if(RPS_df.iloc[i,0][2] == 'Y'):
            score += 4 # 1 + 3
        if(RPS_df.iloc[i,0][2] == 'Z'):
            score += 8 # 2 + 6
    if(RPS_df.iloc[i,0][0] == 'B'):
        if(RPS_df.iloc[i,0][2] == 'X'):
            score += 1 # 1 + 0
        if(RPS_df.iloc[i,0][2] == 'Y'):
            score += 5 # 2 + 3
        if(RPS_df.iloc[i,0][2] == 'Z'):
            score += 9 # 3 + 6
    if(RPS_df.iloc[i,0][0] == 'C'):
        if(RPS_df.iloc[i,0][2] == 'X'):
            score += 2 # 2 + 0
        if(RPS_df.iloc[i,0][2] == 'Y'):
            score += 6 # 3 + 3
        if(RPS_df.iloc[i,0][2] == 'Z'):
            score += 7 # 1 + 6
print(score)