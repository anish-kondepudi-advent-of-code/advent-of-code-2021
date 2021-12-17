
def readfile(filename):
    with open(filename) as file:
        line = file.readlines()[0].strip()
        t1,t2,x,y = line.split()
        x = x.split('=')[-1][:-1]
        y = y.split('=')[-1]
        x1,x2 = map(int,x.split('..'))
        y1,y2 = map(int,y.split('..'))
        return x1,x2,y1,y2

def findMaxHeight(x1,x2,y1,y2,vx,vy):
    maxHeight = 0
    x,y = 0,0
    while True:
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        maxHeight = max(maxHeight,y)
        if (x1<=x<=x2) and (y1<=y<=y2):
            return (True,maxHeight)
        if x>x2 or y<y1:
            return (False,-1)


def part1(filename,size):
    x1,x2,y1,y2 = readfile(filename)
    maxHeight = 0
    for i in range(x2+1):
        for j in range(y1-1,size):
            valid,height = findMaxHeight(x1,x2,y1,y2,i,j)
            if valid:
                maxHeight = max(maxHeight,height)
    return maxHeight

def part2(filename,size):
    x1,x2,y1,y2 = readfile(filename)
    numValid = 0
    for i in range(x2+1):
        for j in range(y1-1,size):
            if i==0 and j==0: continue
            valid,height = findMaxHeight(x1,x2,y1,y2,i,j)
            numValid += (1 if valid else 0)
    return numValid

# Brute Force with Arbitrary Size Param (Hacky Solution)
print(part1("input.txt",250))
print(part2("input.txt",250))
