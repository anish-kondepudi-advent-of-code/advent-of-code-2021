
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

def operations(parentID,vals):
    if parentID == 0:
        return sum(vals)
    elif parentID == 1:
        return eval('*'.join(str(num) for num in vals))
    elif parentID == 2:
        return min(vals)
    elif parentID == 3:
        return max(vals)
    elif parentID == 5:
        return int(vals[0]>vals[1])
    elif parentID == 6:
        return int(vals[0]<vals[1])
    else:
        return int(vals[0]==vals[1])

def decodePacket(packet,i,j):
    # Base Case
    if binToDec(packet[i:j]) == 0:
        return None, None

    packetVal = binToDec(packet[i:i+3])
    packetID = binToDec(packet[i+3:i+6])

    if packetID == 4:
        # Handle Literals
        i = i+6
        packetSumStr = ""
        while int(packet[i]):
            packetSumStr += packet[i+1:i+5]
            i += 5
        packetSumStr += packet[i+1:i+5]
        return binToDec(packetSumStr),i+5

    else:
        i = i+7
        if packet[i-1] == '0':
            # 15 Bit Number (Len of Subpackets)
            lenSubpackets = binToDec(packet[i:i+15])
            vals = []
            endOfPacket = i+15+lenSubpackets
            end = 0
            i = i+15
            while end != endOfPacket:
                val,end = decodePacket(packet,i,j)
                vals.append(val)
                i = end
            return operations(packetID,vals), end
        else:
            # 11 Bit Number (Num Subpackets)
            numSubpackets = binToDec(packet[i:i+11])
            i = i+11
            vals = []
            end = 0
            for _ in range(numSubpackets):
                val,end = decodePacket(packet,i,j)
                vals.append(val)
                i = end
            return operations(packetID,vals), end            

def part2(filename):
    hexInput = readfile(filename)
    binInput = hexToBin(hexInput)
    return decodePacket(binInput,0,len(binInput))[0]

print(part1("input.txt"))
print(part2("input.txt"))
