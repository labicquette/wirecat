import pandas as pd
import string

userFile = 'tramedns.txt'
hexa = "0123456789abcdef"
hexa = set(hexa)
f = open(userFile)
cptLine = 0
cptOffset = 0
  
arrayBytes = []
arrayFile = []

for line in f:
    cptLine += 1
    arrayBytes = line.split(" ")
    offset = arrayBytes[0]
    ByteEOL= arrayBytes[len(arrayBytes) - 1]
    #print("ver1",arrayBytes)
    #filtrage de commentaires dans les trames
    for byte in range(1, len(arrayBytes)-1):
        #print(arrayBytes[byte])
        tailleByte = len(arrayBytes[byte])
        if tailleByte > 2 :

            if arrayBytes[byte][2] == "#":
                arrayBytes[byte] = arrayBytes[0] + arrayBytes[1]
                arrayBytes = arrayBytes[:byte + 1]
                break
            if arrayBytes[byte][0] == "#":
                arrayBytes = arrayBytes[:byte]
                break

    if len(ByteEOL) == 3 :
        arrayBytes.append(ByteEOL[0]+ByteEOL[1])
    arrayBytes = list(filter(lambda x : x != '', arrayBytes))
    filteredBytes = list(filter(lambda x : len(x) == 2 , arrayBytes))
    
    if len(filteredBytes) < len(arrayBytes) - 2:
        print("File", userFile,", line",cptLine)
        break
    

    if cptOffset != int(offset,16):
        print("Erreur numero Offset")
        print(line)
        break
    else :
        cptOffset += len(filteredBytes)



    if len(arrayBytes[0]) == 4 :
        filteredBytes = [arrayBytes[0],filteredBytes]
    else :
        arrayBytes = []   
    if filteredBytes != []:
        arrayFile.append(filteredBytes) 
       
for i in arrayFile:
    print(i)
f.close()