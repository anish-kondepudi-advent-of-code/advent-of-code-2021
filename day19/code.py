
from collections import deque
import time

def readfile(filename):
	with open(filename) as file:
		data = []
		pts = []
		for line in file.readlines():
			line = line.strip()
			if line.startswith("---"):
				continue
			elif line == "":
				data.append(pts[:])
				pts = []
			else:
				pts.append(list(map(int,line.split(','))))
		if len(pts) != 0: 
			data.append(pts[:])
		return data

def getDirections(x,y,z):
	return [
			  # x is facing x
			  [x, y, z],
			  [x, -z, y],
			  [x, -y, -z],
			  [x, z, -y],
			  # x is facing -x
			  [-x, -y, z],
			  [-x, -z, -y],
			  [-x, y, -z],
			  [-x, z, y],
			  # x is facing y
			  [-z, x, -y],
			  [y, x, -z],
			  [z, x, y],
			  [-y, x, z],
			  # x is facing -y
			  [z, -x, -y],
			  [y, -x, z],
			  [-z, -x, y],
			  [-y, -x, -z],
			  # x is facing z
			  [-y, -z, x],
			  [z, -y, x],
			  [y, z, x],
			  [-z, y, x],
			  # x is facing -z
			  [z, y, -x],
			  [-y, z, -x],
			  [-z, -y, -x],
			  [y, -z, -x]
			]

def getPossibleOrientations(pts):
	orientations = []
	for x,y,z in pts:
		orientations.append(getDirections(x,y,z))
	return zip(*orientations)

def countMatchesX(x,pts,gridXPts,matches):
	orientations = getPossibleOrientations(pts)
	for orientation in orientations:
		count = 0
		for dx,_,_ in orientation:
			if x+dx in gridXPts:
				count += 1
		if count >= matches:
			return True
	return False

def countMatchesXY(x,y,pts,gridXYPts,matches):
	orientations = getPossibleOrientations(pts)
	for orientation in orientations:
		count = 0
		for dx,dy,_ in orientation:
			if (x+dx,y+dy) in gridXYPts:
				count += 1
		if count >= matches:
			return True
	return False

def countMatchesXYZ(x,y,z,pts,gridXYZPts,matches):
	orientations = getPossibleOrientations(pts)
	for orientation in orientations:
		count = 0
		for dx,dy,dz in orientation:
			if (x+dx,y+dy,z+dz) in gridXYZPts:
				count += 1
		if count >= matches:
			return True
	return False


def findNumScanners(filename,size,matches,debug):
	data = readfile(filename)
	gridXPts = set([coord[0] for coord in data[0]])
	gridXYPts = set([tuple(coord[:2]) for coord in data[0]])
	gridXYZPts = set([tuple(coord) for coord in data[0]])
	scannerPositions = [(0,0,0)]
	queue = deque(data[1:])
	while len(queue) != 0:
		pts = queue.popleft()
		if debug: print(f"dataset: {data.index(pts)}")
		posX, posXY, posXYZ  = [], [], []
		for x in range(-size,size):
			if countMatchesX(x,pts,gridXPts,matches):
				posX.append(x)
				if debug: print(f"posX add: {x}")
		for x in posX:
			for y in range(-size,size):
				if countMatchesXY(x,y,pts,gridXYPts,matches):
					posXY.append((x,y))
					if debug: print(f"posXY add: {x,y}")
		for x,y in posXY:
			for z in range(-size,size):
				if countMatchesXYZ(x,y,z,pts,gridXYZPts,matches):
					posXYZ.append((x,y,z))
					if debug: print(f"posXYZ add: {x,y,z}")
		if len(posXYZ) == 0:
			queue.append(pts)
			continue
		x,y,z = posXYZ[0]
		scannerPositions.append((x,y,z))
		orientations = getPossibleOrientations(pts)
		for orientation in orientations:
			count = 0
			newBeacons = set()
			for di,dj,dk in orientation:
				ni,nj,nk = di+x,dj+y,dk+z
				newBeacons.add((ni,nj,nk))
				if (ni,nj,nk) in gridXYZPts:
					count += 1
			if count >= 12:
				for px,py,pz in newBeacons:
					gridXPts.add(px)
					gridXYPts.add((px,py))
					gridXYZPts.add((px,py,pz))
				if debug: print("Found: ("+str(x)+','+str(y)+','+str(z)+")")
				break
	return scannerPositions,len(gridXYZPts)

def findMaxDistance(scannerPositions):
	maxDist = 0
	for i in range(len(scannerPositions)):
		for j in range(i+1,len(scannerPositions)):
			x1,y1,z1 = scannerPositions[i]
			x2,y2,z2 = scannerPositions[j]
			dist = abs(x2-x1)+abs(y2-y1)+abs(z2-z1)
			maxDist = max(maxDist,dist)
	return maxDist

def solve(filename,size,matches,debug):
	start_time = time.time()
	scannerPositions, numScanners = findNumScanners(filename,size,matches,debug)
	maxDistance = findMaxDistance(scannerPositions)
	print(f"{numScanners=}")
	print(f"{maxDistance=}")
	if debug: print("--- %s seconds ---" % (time.time() - start_time))

# Arbitrary Size Value Based on Input
solve("input.txt",10000,12,True)
