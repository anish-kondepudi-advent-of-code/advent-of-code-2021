
from copy import deepcopy

def readfile(filename):
	with open(filename) as file:
		lines = [line.strip() for line in file.readlines()]
		image = []
		for line in lines[2:]:
			row = []
			for char in line:
				row.append(char)
			image.append(row)
		return lines[0], image

def printImage(image):
	for row in image:
		print(*row,sep="")
	print("------")

def inBounds(i,j,image):
	return 0<=i<len(image) and 0<=j<len(image[0])

def getPosition(i,j,image):
	pos = 0
	for row in range(i-1,i+2):
		for col in range(j-1,j+2):
			pos <<= 1
			if inBounds(row,col,image):
				cell = image[row][col]
				pos += int(cell=='#')
	return pos

def enhance(algorithm,image,iter):
	margin = 10
	char = '#' if iter and algorithm[0]=='#' and algorithm[-1]=='.' else '.'

	oldImage = []
	rowPart = [char for _ in range(margin//2)]
	fullRow = [char for _ in range(margin+len(image[0]))]
	for _ in range(margin//2):
		oldImage.append(deepcopy(fullRow))
	for row in image:
		oldImage.append(deepcopy(rowPart)+row+deepcopy(rowPart))
	for _ in range(margin//2):
		oldImage.append(deepcopy(fullRow))

	newImage = [['.' for _ in range(len(oldImage[0]))] for _ in range(len(oldImage))]
	for i in range(len(oldImage)):
		for j in range(len(oldImage)):
			pos = getPosition(i,j,oldImage)
			newImage[i][j] = algorithm[pos]

	outputImage = []
	for row in newImage[4:-3]:
		outputImage.append(row[4:-3])

	return outputImage

def findNumLit(image):
	numLit = 0
	for row in image:
		for cell in row:
			numLit += int(cell=='#')
	return numLit

def solve(filename,iterations):
	algorithm, image = readfile(filename)
	oldImage,newImage = image,image
	for i in range(iterations):
		oldImage = newImage
		newImage = enhance(algorithm,oldImage,i%2!=0)
	return findNumLit(newImage)

print(solve("input.txt",2))
print(solve("input.txt",50))