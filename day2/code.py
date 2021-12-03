
def readfile(filename):
    with open("input.txt") as file:
        lines = []
        for line in file.readlines():
            direction, amount = line.split()
            lines.append((direction,int(amount)))
        return lines

def findSubmarinePosition1(filename):
    lines = readfile(filename)
    x,y = 0,0
    for direction, amount in lines:
        if direction == "up":
            y -= amount
        elif direction == "down":
            y += amount
        else:
            x += amount
    return x*y

def findSubmarinePosition2(filename):
    lines = readfile(filename)
    x,y,aim = 0,0,0
    for direction, amount in lines:
        if direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount
        else:
            x += amount
            y += aim*amount
    return x*y


print(findSubmarinePosition1("input.txt"))
print(findSubmarinePosition2("input.txt"))

