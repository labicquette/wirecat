import ethernet


def decoder(dictBytes={}):
    dictInfos = {}
    if dictBytes == {}:
        return {"Trame non valide ou vide":""}
    else:
        for trame in dictBytes:
                dictInfos[trame] = {}
                dictInfos[trame] = ethernet.analyser(dictInfos[trame],dictBytes[trame])
        return dictInfos
        
