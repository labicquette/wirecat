supportedProtocols = {}
def analyser(dictTrame, startOFFset, arrayBytes=[]):
    sO = startOFFset
    dictInfos = {}
    source_port=convertToString(arrayBytes[sO:sO+2])
    dictInfos['Source port'] = str(convertToInt(source_port))
    dest_port=convertToString(arrayBytes[sO+2:sO+4])
    dictInfos['Destination port'] = str(convertToInt(dest_port))
    length = convertToString(arrayBytes[ 4 + sO:sO + 6]) 
    dictInfos['Length'] = str(convertToInt(length)) + "(" + length + ")"
    dictInfos['Checksum'] = convertToString(arrayBytes[6 + sO : 8 + sO])
    return dictInfos
    
def getProtocol(port, dictTrame, arrayBytes, startOFFset):
    if port in supportedProtocols:
        if port == "53":
            return dns.analyser(dictTrame, startOFFset, arrayBytes)
    else :
        return "Protocol not supported"

def protocols(dictTrame, arrayBytes, startOFFset, source_port, dest_port):
    source = int(source_port, 16)
    destination = int(source_port, 16)
    if source < 1024:
        getProtocol(source, dictTrame, arrayBytes, startOFFset)
    else:
        if destination < 1024:
            getProtocol(destination)
        else : return "Not supported data"
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