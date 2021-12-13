
def readfile(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
        coords, folds = [], []
        maxX, maxY = -1, -1
        part = 0
        for line in lines:
            if line == "":
                part = 1
            elif part == 0:
                x,y = tuple(map(int,line.split(",")))
                coords.append((x,y))
                maxX = max(maxX,x)
                maxY = max(maxY,y)
            else:
                fold = line.split()[-1]
                direction, amount = fold.split("=")
                folds.append((direction,int(amount)))
        return (coords,folds,maxX,maxY)

def printGrid(grid):
    for row in grid:
        print(*row,sep="")

def constructGrid(maxX,maxY,coords):
    grid = [["." for _ in range(maxX+1)] for _ in range(maxY+1)]
    for x,y in coords:
        grid[y][x] = '#'
    return grid

def flipY(grid,flipY):
    dimX, dimY = len(grid[0]), len(grid)
    newGrid = [['.' for _ in range(dimX)] for _ in range(flipY)]
    y_up, y_down = flipY, flipY
    while y_up >= 0:
        for x in range(dimX):
            if grid[y_up][x] == '#':
                newGrid[y_up][x] = '#'
            if y_down < dimY and grid[y_down][x] == '#':
                newGrid[y_up][x] = '#'
        y_up -= 1
        y_down += 1
    return newGrid

def flipX(grid,flipX):
    dimX, dimY = len(grid[0]), len(grid)
    newGrid = [['.' for _ in range(flipX)] for _ in range(dimY)]
    x_left, x_right = flipX, flipX
    while x_left >= 0:
        for y in range(dimY):
            if grid[y][x_left] == '#':
                newGrid[y][x_left] = '#'
            if x_right < dimX and grid[y][x_right] == '#':
                newGrid[y][x_left] = '#'
        x_left -= 1
        x_right += 1
    return newGrid

def countDots(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell == "#":
                count += 1
    return count

def findDots(filename):
    coords, folds, maxX, maxY = readfile(filename)
    grid = constructGrid(maxX,maxY,coords)
    count = -1
    for direction, amount in folds:
        if direction == 'y':
            grid = flipY(grid,amount)
        else:
            grid = flipX(grid,amount)
        if count == -1:
            count = countDots(grid)
    printGrid(grid)
    return count



print(findDots("input.txt"))

