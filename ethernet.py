import ipv4
supportedProtocols = {"0800"}

def analyser(dictTrame, arrayBytes=[]):
    dictInfos = {}
    mac1 = ''
    mac2 = ''
    for i in range(0, 6):
        mac1 += arrayBytes[i] 
        mac2 += arrayBytes[i+6]
        if i != 5 :
            mac1 += ":"
            mac2 += ":"
    Type = arrayBytes[12] + arrayBytes[13] 
    dictInfos['Destination'] = mac1
    dictInfos['Source'] = mac2
    if Type in supportedProtocols:
        dictInfos['Type'] = protocolName(Type) + "(" + Type + ")"
        dictInfos[Type] = protocols(Type, dictTrame, arrayBytes)
    else :
        dictInfos['Type'] = Type + " Protocol not supported"
    
    return dictInfos


def protocols(protocol, dictTrame, arrayBytes):

    if protocol == "0800":
        return ipv4.analyser(dictTrame, 14, arrayBytes)
        
def protocolName(protocol):

    if protocol == "0800":
        return "IPV4 "