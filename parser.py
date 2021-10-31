import pandas as pd

df = pd.read_csv("trame1.txt", sep='\s+',index_col=0, skip_blank_lines=True, header=None, dtype=str)
for i in df:
    print(df[i][20])
print(df)