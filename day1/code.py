
def readfile(filename):
    with open("input.txt") as file:
        return [int(line.rstrip()) for line in file.readlines()]


def findIncreasingCount1(filename):
    lines = readfile(filename)
    count,i = 0,1
    while i < len(lines):
        count += (lines[i]>lines[i-1])
        i += 1
    return count

def findIncreasingCount2(filename):
    lines = readfile(filename)
    count,i = 0,0
    prevWindow = float('inf')
    while i < len(lines)-2:
        currWindow = sum(lines[i:i+3])
        count += (currWindow>prevWindow)
        prevWindow = currWindow
        i += 1
    return count

print(findIncreasingCount1("input.txt"))
print(findIncreasingCount2("input.txt"))

