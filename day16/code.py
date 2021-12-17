
def readfile(filename):
    with open(filename) as file:
        return file.readlines()[0].strip()

def binToDec(binStr):
    dec = 0
    for bit in binStr:
        dec <<= 1
        dec += int(bit)
    return dec

def hexToBin(hexStr):
    hexMap = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', 
            '4':'0100', '5':'0101', '6':'0110', '7':'0111', 
            '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 
            'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    binStr = ""
    for c in hexStr:
        binStr += hexMap[c]
    return binStr

def findPacketVersionSum(binStr):
    # Base Case
    if binToDec(binStr) == 0:
        return 0
    # Recurse
    packetVal = binToDec(binStr[:3])
    packetID = binToDec(binStr[3:6])
    binStr = binStr[6:]
    if packetID == 4:
        # Handle Literals
        i = 0
        packetSumStr = ""
        while int(binStr[i]):
            packetSumStr += binStr[i+1:i+5]
            i += 5
        packetSumStr += binStr[i+1:i+5]
        packetSum = binToDec(packetSumStr)
        return packetVal+findPacketVersionSum(binStr[i+5:])
    else:
        lengthTypeID = binStr[0]
        if lengthTypeID == '0':
            # 15 Bit Number (Len of Subpackets)
            lenSubpackets = binToDec(binStr[1:16])
            return packetVal+findPacketVersionSum(binStr[16:16+lenSubpackets])+findPacketVersionSum(binStr[16+lenSubpackets:])
        else:
            # 11 Bit Number (Num Subpackets)
            return packetVal+findPacketVersionSum(binStr[12:])
    # Safety Return (Never Fires)
    return 0


def part1(filename):
    hexInput = readfile(filename)
    binInput = hexToBin(hexInput)
    return findPacketVersionSum(binInput)

def operations(parentID,r1,r2):
    if r2 == -1:
        return r1
    elif parentID == 0:
        return r1+r2
    elif parentID == 1:
        return r1*r2
    elif parentID == 2:
        return min(r1,r2)
    elif parentID == 3:
        return max(r1,r2)
    elif parentID == 5:
        return (1 if r1 > r2 else 0)
    elif parentID == 6:
        return (1 if r1 < r2 else 0)
    else:
        return (1 if r1 == r2 else 0)

afterStr = ""

def decodePacket(binStr,numPackets,parentID):
    # Base Case
    if binToDec(binStr) == 0:
        return -1
    # Recurse
    packetVal = binToDec(binStr[:3])
    packetID = binToDec(binStr[3:6])
    binStr = binStr[6:]
    if packetID == 4:
        # Handle Literals
        i = 0
        packetSumStr = ""
        while int(binStr[i]):
            packetSumStr += binStr[i+1:i+5]
            i += 5
        packetSumStr += binStr[i+1:i+5]
        r1 = binToDec(packetSumStr)
        r2 = decodePacket(binStr[i+5:],numPackets-1,parentID)
        print(r1,r2,parentID,operations(parentID,r1,r2))
        return operations(parentID,r1,r2)
    else:
        lengthTypeID = binStr[0]
        if lengthTypeID == '0':
            # 15 Bit Number (Len of Subpackets)
            lenSubpackets = binToDec(binStr[1:16])
            r1 = decodePacket(binStr[16:16+lenSubpackets],-1,packetID)
            r2 = decodePacket(binStr[16+lenSubpackets:],numPackets-1,packetID)
            return operations(parentID,r1,r2)
        else:
            # 11 Bit Number (Num Subpackets)
            numSubpackets = binToDec(binStr[1:12])
            r1 = decodePacket(binStr[12:],numSubpackets,packetID)
            # NEED TO SPLIT THIS
    # Safety Return (Never Fires)
    return 0

def part2(filename):
    hexInput = readfile(filename)
    binInput = hexToBin(hexInput)
    return decodePacket(binInput,-1,0)

print(part1("input.txt"))
# print(part2("input.txt")  )
