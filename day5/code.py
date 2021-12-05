
def readfile(filename):
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file.readlines()]
        result = []
        for line in lines:
            x,y = line.split("->")
            x1,y1 = list(map(int,x.split(',')))
            x2,y2 = list(map(int,y.split(',')))
            result.append((x1,y1,x2,y2))
        return result

def printMatrix(matrix):
    for row in [*zip(*matrix)]:
        for num in row:
            print(f"{num} ",end='')
        print()
    print("-----")

def overlap1(filename):
    lines = readfile(filename)

    maxX, maxY = 0, 0
    for x1,y1,x2,y2 in lines:
        maxX = max(maxX,max(x1,x2))
        maxY = max(maxY,max(y1,y2))

    matrix = [[0 for i in range(maxX+2)] for j in range(maxY+2)]

    for x1,y1,x2,y2 in lines:
        if x1 == x2:
            # Vertical Line
            for y in range(min(y1,y2),max(y1,y2)+1):
                matrix[x1][y] += 1
        elif y1 == y2:
            # Horizontal Line
            for x in range(min(x1,x2),max(x1,x2)+1):
                matrix[x][y1] += 1

    points = 0
    for row in matrix:
        for num in row:
            if num > 1:
                points += 1

    return points

def overlap2(filename):
    lines = readfile(filename)

    maxX, maxY = 0, 0
    for x1,y1,x2,y2 in lines:
        maxX = max(maxX,max(x1,x2))
        maxY = max(maxY,max(y1,y2))

    matrix = [[0 for i in range(maxX+2)] for j in range(maxY+2)]

    for x1,y1,x2,y2 in lines:
        if x1 == x2:
            # Vertical Line
            for y in range(min(y1,y2),max(y1,y2)+1):
                matrix[x1][y] += 1
        elif y1 == y2:
            # Horizontal Line
            for x in range(min(x1,x2),max(x1,x2)+1):
                matrix[x][y1] += 1
        else:
            # Diagonal
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            while x1 <= x2:
                matrix[x1][y1] += 1
                x1 += 1
                y1 += (1 if y1<=y2 else -1)

    points = 0
    for row in matrix:
        for num in row:
            if num > 1:
                points += 1

    return points

print(overlap1("input.txt"))
print(overlap2("input.txt"))

