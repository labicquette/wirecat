import pandas as pd
import string

df = pd.read_csv("trame1.txt", sep='\s+',index_col=0, skip_blank_lines=True, header=None, dtype=str, comment='#')

#for i in df:
#    print(df[][i])
#print(df)
hexa = "0123456789abcdef"
hexa = set(hexa)
f = open('trame1.txt')


arrayBytes = []
arrayFile = []
for line in f:
    arrayBytes = line.split(" ")
    offset = arrayBytes[0]
    ByteEOL= arrayBytes[len(arrayBytes) - 1]

    print(arrayBytes)
    for byte in range(1, len(arrayBytes)):
        #print(arrayBytes[byte])
        print(arrayBytes[byte])
        tailleByte = len(arrayBytes[byte])
        if tailleByte > 2 :

            if arrayBytes[byte][2] == "#":
                arrayBytes[byte] = arrayBytes[byte][0] + arrayBytes[byte][1]
                arrayBytes = arrayBytes[:byte]
                break
        
        else :
            if(arrayBytes[byte][0] == "#"):
                arrayBytes = arrayBytes[:byte]
                break

    #ByteEOL 

    filteredBytes = list(filter(lambda x : len(x) == 2, arrayBytes))
    #filteredBytes.append()


    #if len(filteredBytes) + 1
    if len(arrayBytes[0]) == 4 :
        filteredBytes = [arrayBytes[0],filteredBytes]
    else :
        arrayBytes = []    
       
    if arrayBytes != []:
        arrayFile.append(arrayBytes)
for i in arrayFile:
    print(i)
f.close()