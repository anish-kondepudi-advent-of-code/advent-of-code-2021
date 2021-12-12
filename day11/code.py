
def readfile(filename):
    with open(filename) as file:
        return [list(map(int,list(line.strip()))) for line in file.readlines()]

def inBounds(matrix,i,j):
    return 0<=i<len(matrix) and 0<=j<len(matrix[0])

def dfs(flashed,octopuses):
    numFlashed = len(flashed)
    hasFlashed = set(flashed)
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), 
                (0,1), (1,-1), (1,0), (1,1)]
    while len(flashed) != 0:
        i,j = flashed.pop()
        for di, dj in directions:
            ni, nj = i+di, j+dj
            if inBounds(octopuses,ni,nj) and (ni,nj) not in hasFlashed:
                energyLevel = octopuses[ni][nj]
                if energyLevel < 9:
                    octopuses[ni][nj] += 1
                else:
                    octopuses[ni][nj] = 0
                    flashed.append((ni,nj))
                    hasFlashed.add((ni,nj))
                    numFlashed += 1
    return numFlashed

def step(octopuses):
    flashed = []
    for i in range(len(octopuses)):
        for j in range(len(octopuses[0])):
            energyLevel = octopuses[i][j]
            if energyLevel < 9:
                octopuses[i][j] += 1
            else:
                octopuses[i][j] = 0
                flashed.append((i,j))
    return dfs(flashed,octopuses)

def findTotalFlashes(filename,steps):
    octopuses = readfile(filename)
    flashes = 0
    for _ in range(steps):
        flashes += step(octopuses)
    return flashes

def findAllFlashesStep(filename):
    octopuses = readfile(filename)
    maxFlashes = len(octopuses)*len(octopuses[0])
    itr = 1
    while True:
        if step(octopuses) == maxFlashes:
            return itr
        itr += 1
    return
    
print(findTotalFlashes("input.txt",100))
print(findAllFlashesStep("input.txt"))


