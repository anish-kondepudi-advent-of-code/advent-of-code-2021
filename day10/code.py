
def readfile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]

def findComplement(opening):
    return ")]}>"["([{<".index(opening)]

def findFirstError(line):
    stack = []
    for c in line:
        if c in "([{<":
            stack.append(findComplement(c))
        else:
            if len(stack) == 0: return c
            char = stack.pop()
            if char != c: return c
    return ' '

def findEndingString(line):
    stack = []
    for c in line:
        if c in "([{<":
            stack.append(findComplement(c))
        else:
            if len(stack) == 0: return (False,'')
            char = stack.pop()
            if char != c: return (False,'')
    if len(stack) == 0:
        return (False,'')
    endingString = ''
    while len(stack) != 0:
        endingString += stack.pop()
    return (True,endingString)


def syntaxScore1(filename):
    lines = readfile(filename)
    scores = {' ':0, ')':3, ']':57, '}':1197, '>':25137}
    score = 0
    for line in lines:
        char = findFirstError(line)
        score += scores[char]
    return score

def syntaxScore2(filename):
    lines = readfile(filename)
    scoreMap = {')':1, ']':2, '}':3, '>':4}
    scores = []
    for line in lines:
        hasEndStr, endStr = findEndingString(line)
        if hasEndStr:
            score = 0
            for c in endStr:
                score *= 5
                score += scoreMap[c]
            scores.append(score)
    scores = sorted(scores)
    return scores[len(scores)//2]

print(syntaxScore1("input.txt"))
print(syntaxScore2("input.txt"))

