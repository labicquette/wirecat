


def analyser(dictTrame, startOFFset, arrayBytes=[]):
    sO = startOFFset
    dictInfos = {}
    dictInfos['Version'] = arrayBytes[sO]
    dictInfos['IHL (Internet Header Length)'] = arrayBytes[sO + 1]
    dictInfos['Differentiated Services'] = differentiatedServices(arrayBytes[2+sO:4+sO]) 
    totalLength = convertToString(arrayBytes[4 + sO:8 + sO]) 
    dictInfos['Total Length'] = str(convertToInt(totalLength)) + "(" + totalLength + ")"
    dictInfos['Indentification'] = str(convertToInt(arrayBytes[8 + sO : 12 + sO]))
    #dictInfos['Flags'] = flags(arrayBytes[12 + sO : 15 + sO])
    return dictInfos





#def flags(arrayBytes=[])

def differentiatedServices(arrayBytes=[]):
    service = convertToInt(arrayBytes)
    
    if service < 4 or service > 9:
        return "Reserved"
    if service == 4 :
        return "IP, Internet Protocol"
    if service == 5 :
        return "ST, Datagram Mode"
    if service == 6 : 
        return "IPV, Internet Protocol"
    if service == 7 :
        return "TP/IX, The Next Internet"
    if service == 8 :
        return "PIP, The P Internet Protocol"
    if service == 9 :
        return "TUBA"


MOD = 1 << 32
def onesCompAdd16(num1,num2):
    result = num1 + num2 
    return result if result < MOD else(result + 1) % MOD
 

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