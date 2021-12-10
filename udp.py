def analyser(dictTrame, startOFFset, arrayBytes=[]):
    sO = startOFFset
    dictInfos = {}
    source_port=convertToString(arrayBytes[sO:sO+3])
    dictInfos['source port number'] = str(convertToInt(source_port))
    dest_port=convertToString(arrayBytes[sO+4:sO+7])
    dictInfos['destination port number'] = str(convertToInt(dest_port))
    length = convertToString(arrayBytes[8 + sO:sO+11]) 
    dictInfos['Length'] = str(convertToInt(length)) + "(" + length + ")"
    dictInfos['checksum'] = convertToString(arrayBytes[12 + sO : 15 + sO])
    #dictInfos['Flags'] = flags(arrayBytes[12 + sO : 15 + sO])
    return dictInfos
    
def convertToString(args=[]):
    string = ''
    for i in args:
        string += i
    return string


def convertToInt(args=[]):
    string = ''
    for i in args:
        string += i
    return int(string,16)