import pandas as pd
import re

df = pd.read_csv("trame1.txt", sep='\s+',index_col=0, skip_blank_lines=True, header=None, dtype=str, comment='#')

#for i in df:
#    print(df[][i])
#print(df)

f = open('trame1.txt')

offset = 0

for line in f: 
    #match = re.findall("^[0-9a-f]{4} ([0-9a-f]{2} ?)*$",line)
    exp = r'^([0-9a-f]{4})( [0-9a-f]{2})* ?#?.*$'
    #exp2 = ' [0-9a-f]{2}'
    match = re.findall(exp, line)
    #match2 = re.findall(exp2, line)
    print(match)
    #print(match2)
    #print(match.group(0))

f.close()