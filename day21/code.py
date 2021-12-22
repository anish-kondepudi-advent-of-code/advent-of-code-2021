
def readfile(filename):
	with open(filename) as file:
		lines = [int(line.strip()[-1]) for line in file.readlines()]
		return tuple(lines)

class DeterministicDice:
	def __init__(self,sides):
		self.roll = 1
		self.sides = sides
	def getRollVal(self):
		val = self.roll
		self.roll = self.roll%self.sides+1
		return val
	def getRollSum(self):
		return sum([self.getRollVal() for _ in range(3)])

def getNewPosition(currPos,steps):
	return ((currPos-1)+steps)%10+1

def part1(filename):
	pos1, pos2 = readfile(filename)
	score1, score2 = 0,0
	dd = DeterministicDice(100)
	rolls = 0
	while True:
		pos1 = getNewPosition(pos1,dd.getRollSum())
		score1 += pos1
		rolls += 3
		if score1 >= 1000: break
		pos2 = getNewPosition(pos2,dd.getRollSum())
		score2 += pos2
		rolls += 3
		if score2 >= 1000: break
	return min(score1,score2)*rolls

def findWinnerDiracDice(pos1,pos2,score1,score2,turn,maxScore,memo):
	# Base Cases
	if score2 >= maxScore:
		return (0,1)
	if score1 >= maxScore:
		return (1,0)
	if (pos1,pos2,score1,score2,turn) in memo:
		return memo[(pos1,pos2,score1,score2,turn)]
	# Recurse
	w1,w2 = 0,0
	s1,s2 = 0,0
	if turn == 1:
		for d1 in range(1,4):
			for d2 in range(1,4):
				for d3 in range(1,4):
					rollVal = d1+d2+d3
					newPos = getNewPosition(pos1,rollVal)
					s1,s2 = findWinnerDiracDice(newPos,pos2,score1+newPos,score2,2,maxScore,memo)
					w1 += s1
					w2 += s2
	else:
		for d1 in range(1,4):
			for d2 in range(1,4):
				for d3 in range(1,4):
					rollVal = d1+d2+d3
					newPos = getNewPosition(pos2,rollVal)
					s1,s2 = findWinnerDiracDice(pos1,newPos,score1,score2+newPos,1,maxScore,memo)
					w1 += s1
					w2 += s2
	# Return
	memo[(pos1,pos2,score1,score2,turn)] = (w1,w2)
	return (w1,w2)

def part2(filename):
	pos1, pos2 = readfile(filename)
	memo = {}
	return max(findWinnerDiracDice(pos1,pos2,0,0,1,21,memo))


print(part1("input.txt"))
print(part2("input.txt"))