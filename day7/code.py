def readfile(filename):
    with open("input.txt") as file:
        return list(map(int,file.readlines()[0].split(',')))

def crab1(filename):
    crabs = readfile(filename)
    minCrab = min(crabs)
    maxCrab = max(crabs)
    idealFuel = float('inf')
    for pos in range(minCrab,maxCrab+1):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab-pos)
        idealFuel = min(idealFuel,fuel)
    return idealFuel

def crab2(filename):
    crabs = readfile(filename)
    minCrab = min(crabs)
    maxCrab = max(crabs)
    idealFuel = float('inf')
    for pos in range(minCrab,maxCrab+1):
        fuel = 0
        for crab in crabs:
            N = abs(crab-pos)
            fuel += (N*(N+1))//2
        idealFuel = min(idealFuel,fuel)
    return idealFuel


print(crab1("input.txt"))
print(crab2("input.txt"))