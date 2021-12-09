
def parser(f):
    cptLine = 0
    cptOffset = 0
    cptTrames = -1

    arrayBytes = []
    dictFrames = {}

    for line in f:
        cptLine += 1
        arrayBytes = line.split(" ")
        offset = arrayBytes[0]
        ByteEOL= arrayBytes[len(arrayBytes) - 1]

        #filtrage de commentaires dans les trames
        for byte in range(1, len(arrayBytes)-1):
            tailleByte = len(arrayBytes[byte])
            if tailleByte > 2 :
                if arrayBytes[byte][2] == "#":
                    arrayBytes[byte] = arrayBytes[0] + arrayBytes[1]
                    arrayBytes = arrayBytes[:byte + 1]
                    break
                if arrayBytes[byte][0] == "#":
                    arrayBytes = arrayBytes[:byte]
                    break
        #integration du dernier Byte de la ligne et suppression du caractere fin de ligne
        if len(ByteEOL) == 3 :
            arrayBytes.append(ByteEOL[0]+ByteEOL[1])
        
        #filtrage des tabulations > 1 espace
        arrayBytes = list(filter(lambda x : x != '', arrayBytes))
        #filtrage des bytes avec len(x) != 2
        filteredBytes = list(filter(lambda x : len(x) == 2 , arrayBytes))

        # verification du bon nombre de bytes     
        if len(filteredBytes) < len(arrayBytes) - 2:
            #print("File", f.name,", line",cptLine)
            return {'Erreur' : "Fichier : '"+ f.name + "'  line : " + str(cptLine)}
            break
    
        #verification nb bytes = offset 
        if cptOffset != int(offset,16):
            return {"Erreur": "Offset : " + line}
        else :
            cptOffset += len(filteredBytes)


        #ajout de l'offset 
        if len(arrayBytes[0]) == 4 :
            if arrayBytes[0] == "0000":
                cptTrames += 1
                dictFrames[cptTrames] = []
        else :
            arrayBytes = []   
        if filteredBytes != []:
            dictFrames[cptTrames] += filteredBytes

    f.close()

    return dictFrames