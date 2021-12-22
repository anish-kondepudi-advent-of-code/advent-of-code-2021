
def readfile(filename):
	with open(filename) as file:
		steps = []
		for line in file.readlines():
			typeSwitch,coords = line.strip().split()
			x,y,z = coords.split(',')
			x1,x2 = map(int,x.split('=')[1].split('..'))
			y1,y2 = map(int,y.split('=')[1].split('..'))
			z1,z2 = map(int,z.split('=')[1].split('..'))
			steps.append((typeSwitch,x1,x2,y1,y2,z1,z2))
		return steps

def part1(filename,area):
	steps = readfile(filename)
	switches = set()
	for typeSwitch,x1,x2,y1,y2,z1,z2 in steps:
		notValid = [x1<-area or y1<-area or z1<-area or 
					x2>area or y2>area or z2>area]
		if any(notValid): continue
		if typeSwitch == 'on':
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					for z in range(z1,z2+1):
						switches.add((x,y,z))
		else:
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					for z in range(z1,z2+1):
						if (x,y,z) in switches:
							switches.remove((x,y,z))
	return len(switches)


def part2(filename):
	steps = readfile(filename)
	# Divide Into Partitions (compressedGrid)
	X,Y,Z = set(),set(),set()
	for _,x1,x2,y1,y2,z1,z2 in steps:
		X.add(x1);X.add(x2+1)
		Y.add(y1);Y.add(y2+1)
		Z.add(z1);Z.add(z2+1)
	X = sorted(list(X))
	Y = sorted(list(Y))
	Z = sorted(list(Z))
	compressedGrid = [[[0 for _ in range(len(Z))] for _ in range(len(Y))] for _ in range(len(X))]
	# Update Compressed Grid based on typeSwitch
	for typeSwitch,x1,x2,y1,y2,z1,z2 in steps:
		value = int(typeSwitch=='on')
		sx,ex = X.index(x1),X.index(x2+1)
		sy,ey = Y.index(y1),Y.index(y2+1)
		sz,ez = Z.index(z1),Z.index(z2+1)
		for x in range(sx,ex):
			for y in range(sy,ey):
				for z in range(sz,ez):
					compressedGrid[x][y][z] = value
	# Find Volume
	volume = 0 
	for x in range(len(compressedGrid)):
		for y in range(len(compressedGrid[0])):
			for z in range(len(compressedGrid[0][0])):
				if compressedGrid[x][y][z]:
					volume += (X[x+1]-X[x])*(Y[y+1]-Y[y])*(Z[z+1]-Z[z])
	return volume

print(part1("input.txt",50))
print(part2("input.txt"))