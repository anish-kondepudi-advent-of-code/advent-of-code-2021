
def readfile(filename):
    with open("input.txt") as file:
        return [line.rstrip() for line in file.readlines()]


def powerConsumption(filename):
    lines = readfile(filename)
    gammaBitstring = [0]*len(lines[0])
    for line in lines:
        for i, bit in enumerate(line):
            gammaBitstring[i] += int((int(bit=='1')-0.5)*2)
    gammaBitstring = [int(x>0) for x in gammaBitstring]
    gamma, epsilon = 0,0
    for bit in gammaBitstring:
        gamma <<= 1
        epsilon <<= 1
        gamma += (bit==1)
        epsilon += (bit==0)
    return gamma*epsilon

def lifeSupport(filename):
    lines = readfile(filename)
    
    O2_Bitstring = [0]*len(lines[0])
    visited = set()
    bitIdx = 0
    while bitIdx < len(lines[0]):
        numZeros, numOnes = 0, 0
        zeroLines, oneLines = [], []
        for i,line in enumerate(lines):
            if i in visited: continue
            bit = int(line[bitIdx])
            if bit == 1:
                numOnes += 1
                oneLines.append(i)
            if bit == 0:
                numZeros += 1
                zeroLines.append(i)
        if numOnes>=numZeros:
            O2_Bitstring[bitIdx] = 1
            for lineIdx in zeroLines:
                visited.add(lineIdx)
        else:
            for lineIdx in oneLines:
                visited.add(lineIdx)
        if len(visited)+1 == len(lines):
            N = len(lines)-1
            idx = N*(N+1)//2 - sum(visited)
            for i,bit in enumerate(lines[idx]):
                O2_Bitstring[i] = int(bit)
            break
        bitIdx += 1

    CO2_Bitstring = [1]*len(lines[0])
    visited = set()
    bitIdx = 0
    while bitIdx < len(lines[0]):
        numZeros, numOnes = 0, 0
        zeroLines, oneLines = [], []
        for i,line in enumerate(lines):
            if i in visited: continue
            bit = int(line[bitIdx])
            if bit == 1:
                numOnes += 1
                oneLines.append(i)
            if bit == 0:
                numZeros += 1
                zeroLines.append(i)
        if numZeros<=numOnes:
            CO2_Bitstring[bitIdx] = 0
            for lineIdx in oneLines:
                visited.add(lineIdx)
        else:
            for lineIdx in zeroLines:
                visited.add(lineIdx)
        if len(visited)+1 == len(lines):
            N = len(lines)-1
            idx = N*(N+1)//2 - sum(visited)
            for i,bit in enumerate(lines[idx]):
                CO2_Bitstring[i] = int(bit)
            break
        bitIdx += 1

    o2, co2 = 0,0
    for bit_o2, bit_co2 in zip(O2_Bitstring,CO2_Bitstring):
        o2 <<= 1
        co2 <<= 1
        o2 += (bit_o2==1)
        co2 += (bit_co2==1)

    return o2*co2

print(powerConsumption("input.txt"))
print(lifeSupport("input.txt"))

