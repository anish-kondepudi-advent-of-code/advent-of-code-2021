def readfile(filename):
    with open(filename) as file:
        return list(map(int,file.readlines()[0].split(',')))

def crabLinear(filename):
    crabs = readfile(filename)
    minCrab, maxCrab = min(crabs), max(crabs)
    idealFuel = float('inf')
    for pos in range(minCrab,maxCrab+1):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab-pos)
        idealFuel = min(idealFuel,fuel)
    return idealFuel

def crabExponential(filename):
    crabs = readfile(filename)
    minCrab, maxCrab = min(crabs), max(crabs)
    idealFuel = float('inf')
    for pos in range(minCrab,maxCrab+1):
        fuel = 0
        for crab in crabs:
            N = abs(crab-pos)
            fuel += N*(N+1)//2
        idealFuel = min(idealFuel,fuel)
    return idealFuel


print(crabLinear("input.txt"))
print(crabExponential("input.txt"))