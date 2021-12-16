
from heapq import heapify, heappush, heappop

def readfile(filename):
    with open(filename) as file:
        return [list(map(int,list(line.strip()))) for line in file.readlines()]

def printMatrix(matrix):
    for row in matrix:
        print(*row,sep="")

def inBounds(matrix,i,j):
    return 0<=i<len(matrix) and 0<=j<len(matrix[0])

def findMinRiskPath(matrix):
    heap = []
    heapify(heap)
    heappush(heap,(0,0,0))
    lastCell = (len(matrix)-1,len(matrix[0])-1)
    visited = set()
    while len(heap) != 0:
        risk,i,j = heappop(heap)
        if (i,j) in visited: continue
        if (i,j) == lastCell: return risk
        visited.add((i,j))
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for di,dj in dirs:
            ni,nj = i+di,j+dj
            if inBounds(matrix,ni,nj):
                heappush(heap,(risk+matrix[ni][nj],ni,nj))
    return -1

def shiftMatrix(matrix,shift):
    newMatrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            newMatrix[i][j] = (matrix[i][j]+shift-1)%9+1
    return newMatrix

def concatenateRows(m1,m2):
    m3 = []
    for r1,r2 in zip(m1,m2):
        m3.append(r1+r2)
    return m3

def getTrueMatrix(matrix,size):
    newMatrix = [[] for _ in range(len(matrix))]
    for shift in range(size):
        newMatrix = concatenateRows(newMatrix,shiftMatrix(matrix,shift))
    firstSizeRowMatrix = [row[:] for row in newMatrix]
    for shift in range(1,size):
        newMatrix += shiftMatrix(firstSizeRowMatrix,shift)
    return newMatrix

def part1(filename):
    matrix = readfile(filename)
    return findMinRiskPath(matrix)

def part2(filename,size):
    matrix = readfile(filename)
    trueMatrix = getTrueMatrix(matrix,size)
    return findMinRiskPath(trueMatrix)
    
print(part1("input.txt"))
print(part2("input.txt",5))


