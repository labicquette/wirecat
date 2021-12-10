import udp


supportedProtocols = {"11": "UDP (User Datagram Protocol)"}

def analyser(dictTrame, startOFFset, arrayBytes=[]):
    sO = startOFFset
    dictInfos = {}
    dictInfos['Version'] = arrayBytes[sO][0]
    dictInfos['IHL (Internet Header Length)'] = arrayBytes[sO][1]
    dictInfos['Differentiated Services'] = differentiatedServices(arrayBytes[1+sO]) 
    totalLength = convertToString(arrayBytes[2 + sO: 4 + sO]) 
    dictInfos['Total Length'] = str(convertToInt(totalLength)) + " (" + totalLength + ")"
    dictInfos['Indentification'] = str(convertToInt(arrayBytes[4 + sO : 6 + sO]))
    dictInfos['Flags'] = flags(arrayBytes[6 + sO])
    dictInfos['Fragment Offset'] = fragmentOFF(arrayBytes[6 + sO:8 + sO])
    dictInfos['Time To Live (TTL)'] = str(int(arrayBytes[8 + sO],16))+ " (" + arrayBytes[8 + sO] + ")"
    dictInfos['Header Checksum'] = arrayBytes[10 + sO]+ arrayBytes[11 + sO]
    dictInfos['Source IP Adress'] = ipConverter(arrayBytes[12 + sO:16 + sO])
    dictInfos['Destination IP Adress'] = ipConverter(arrayBytes[16 + sO : 20 + sO])
    dictInfos['Protocol'] = protocolName(arrayBytes, startOFFset)
    dictInfos['Protocol data'] = protocols(dictTrame, arrayBytes, startOFFset)
    return dictInfos

def ipConverter(listArray=[]):
    res = ""
    for ip in range(0, len(listArray)):
        res += str(int(listArray[ip],16))
        if ip != len(listArray) - 1:
            res += '.'
    return res 

def protocols(dictTrame, arrayBytes, startOFFset):
    protocol = arrayBytes[9 + startOFFset] 
    if protocol in supportedProtocols:
        if  protocol == "11":
            return udp.analyser(dictTrame, startOFFset + (int(arrayBytes[0+startOFFset][1],16) * 4), arrayBytes)
    else :
        return "Protocol not supported :" + protocol
def protocolName(arrayBytes, startOFFset):
    protocol = arrayBytes[9 + startOFFset]
    res = ""
    if int(arrayBytes[1 + startOFFset][1], 16) > 4:
        res = "Options not supported"
    else :
        if protocol in supportedProtocols :
            res = supportedProtocols[protocol]
        else:
            res = "Protocol not supported : " + protocol 
    return res

def fragmentOFF(arrayBytes=[]):
    tempByte = int(arrayBytes[1], 16)
    if int(arrayBytes[0],16) % 2 == 1:
        tempByte += 4096
        return hex(tempByte)
    else:
        return hex(tempByte)

def flags(arrayByte):
    res = ''
    tempByte = int(arrayByte, 16)
    if tempByte >= 8 :
        res += "  Reserved : 1 /"
        tempByte -= 8
    else :
        res += "  Reserved : 0 /"
    if tempByte >= 4 :
        res += " Don't Fragment (DF): 1 /"
        tempByte -= 4
    else:
        res += " Don't Fragment (DF): 0 /"
    if tempByte >= 2 :
        res += " More Fragments (MF): 1"
    else:
        res += " More Fragments (MF): 0"
    return res

def differentiatedServices(arrayBytes=[]):
    service = convertToInt(arrayBytes)
    
    if service < 4 or service > 9:
        return "Reserved " + "(" + str(service) + ")"
    if service == 4 :
        return "IP, Internet Protocol "  + "(" + str(service) + ")"
    if service == 5 :
        return "ST, Datagram Mode "  + "(" + str(service) + ")"
    if service == 6 : 
        return "IPV, Internet Protocol "  + "(" + str(service) + ")"
    if service == 7 :
        return "TP/IX, The Next Internet "  + "(" + str(service) + ")"
    if service == 8 :
        return "PIP, The P Internet Protocol "  + "(" + str(service) + ")"
    if service == 9 :
        return "TUBA"  + "(" + str(service) + ")"


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