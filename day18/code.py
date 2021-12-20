
from math import floor, ceil

def readfile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def explode(line,i):
    # Find [num1,num2]
    di = i
    while line[di] in '0123456789':
        di += 1
    j = i
    while line[j] != ',':
        j += 1
    j += 1
    dj = j
    while line[dj] in '0123456789':
        dj += 1
    num1 = int(line[i:di])
    num2 = int(line[j:dj])
    # Find numleft, numRight
    # Along with corresponding indices
    # ll,lr,rl,rr
    start, end = i-1, dj
    lr,rl = start,end
    while lr >= 0 and line[lr] not in '0123456789':
        lr -= 1
    ll = lr
    while ll >= 0  and line[ll] in '0123456789':
        ll -= 1
    leftNum = line[ll+1:lr+1]
    while rl < len(line) and line[rl] not in '0123456789':
        rl += 1
    rr = rl
    while rr < len(line) and line[rr] in '0123456789':
        rr += 1
    rightNum = line[rl:rr]
    # Create New Exploded Line
    newLine = ''
    if leftNum == '':
        newLine += line[:start]
    else:
        newLine += line[:ll+1]
        newLine += str(int(leftNum)+num1)
        newLine += line[lr+1:start]
    newLine += '0'
    if rightNum == '':
        newLine += line[end+1:]
    else:
        newLine += line[end+1:rl]
        newLine += str(num2+int(rightNum))
        newLine += line[rr:]
    return newLine

def split(line,i):
    di = i
    while line[di] in '0123456789':
        di += 1
    num = int(line[i:di])
    l,r = str(floor(num/2)),str(ceil(num/2))
    return line[:i]+'['+l+','+r+']'+line[di:]

def scanForExplode(line):
    paren = 0
    for i,c in enumerate(line):
        if c == '[':
            paren += 1
        elif c == ']':
            paren -= 1
        if paren == 5:
            return 'explode',i+1
    return 'valid',0

def scanForSplit(line):
    for i,c in enumerate(line):
        if c in '0123456789' and i+1 < len(line) and line[i+1] in '0123456789':
            return 'split',i
    return 'valid',0

def reduce(line):
    while True:
        op, idx = scanForExplode(line)
        if op == 'explode':
            line = explode(line,idx)
            continue
        op, idx = scanForSplit(line)
        if op == 'split':
            line = split(line,idx)
            continue
        break
    return line

def add(line1,line2):
    return reduce('['+line1+','+line2+']')

def leafSum(line):
    for i,c in enumerate(line):
        if c == ',' and line[i-1] in '0123456789' and line[i+1] in '0123456789':
            l,r = i-1,i+1
            while line[l] in '0123456789':
                l -= 1
            while line[r] in '0123456789':
                r += 1
            num1 = int(line[l+1:i])
            num2 = int(line[i+1:r])
            s = str(3*num1+2*num2)
            line = line[:l]+s+line[r+1:]
            return True,line
    return False,line

def findMagnitude(line):
    cont,line = leafSum(line)
    while cont:
        cont,line = leafSum(line)
    return int(line)

def findMagnitudeOfSum(filename):
    lines = readfile(filename)
    line = lines[0]
    for i in range(1,len(lines)):
        line = add(line,lines[i])
    return findMagnitude(line)

def findMaxMagnitudeSum(filename):
    maxSum = 0
    lines = readfile(filename)
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j: continue
            currSum = findMagnitude(add(lines[i],lines[j]))
            maxSum = max(maxSum,currSum)
    return maxSum

print(findMagnitudeOfSum("input.txt"))
print(findMaxMagnitudeSum("input.txt"))

