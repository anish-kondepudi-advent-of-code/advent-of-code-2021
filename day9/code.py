
def readfile(filename):
    with open(filename) as file:
        return [list(map(int,list(line.strip()))) for line in file.readlines()]

def isSink(matrix,i,j):
    isSink = [
        i > 0 and matrix[i][j] >= matrix[i-1][j],
        j > 0 and matrix[i][j] >= matrix[i][j-1],
        i < len(matrix)-1 and matrix[i][j] >= matrix[i+1][j],
        j < len(matrix[0])-1 and matrix[i][j] >= matrix[i][j+1]
    ]
    return not any(isSink)

def findBasinSize(matrix,i,j):
    size = 0
    stack = [(i,j)]
    visited = set()
    while len(stack) != 0:
        i,j = stack.pop()
        if (i,j) in visited: continue
        if matrix[i][j] == 9: continue
        visited.add((i,j))
        size += 1
        if i > 0 and ((i-1,j) not in visited) and matrix[i][j] < matrix[i-1][j]:
            stack.append((i-1,j))
        if j > 0 and ((i,j-1) not in visited) and matrix[i][j] < matrix[i][j-1]:
            stack.append((i,j-1))
        if i < len(matrix)-1 and ((i+1,j) not in visited) and matrix[i][j] < matrix[i+1][j]:
            stack.append((i+1,j))
        if j < len(matrix[0])-1 and ((i,j+1) not in visited) and matrix[i][j] < matrix[i][j+1]:
            stack.append((i,j+1))
    return size

def findMinPointsRiskSum(filename):
    matrix = readfile(filename)
    riskSum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if isSink(matrix,i,j):
                riskSum += matrix[i][j]+1
    return riskSum

def findBasinRiskProduct(filename):
    matrix = readfile(filename)
    basinSizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if isSink(matrix,i,j):
                size = findBasinSize(matrix,i,j)
                # Maintain 3 Largest Sizes
                if len(basinSizes) == 3 and basinSizes[-1] > size:
                    basinSizes[-1] = basinSizes
                else:
                    basinSizes.append(size)
                basinSizes = sorted(basinSizes, reverse=True)
    return basinSizes[0]*basinSizes[1]*basinSizes[2]

print(findMinPointsRiskSum("input.txt"))
print(findBasinRiskProduct("input.txt"))

