
def readfile(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
        template = lines[0]
        pairInsertions = {}
        for line in lines[2:]:
            u,v = line.split(' -> ')
            pairInsertions[u] = v
        return (template,pairInsertions)

def findPolymerStrain(filename,insertions):
    template, pairInsertions = readfile(filename)
    
    templateMap = {}
    for i in range(len(template)-1):
        pair = template[i:i+2]
        if pair not in templateMap:
            templateMap[pair] = 0
        templateMap[pair] += 1

    countMap = {}
    for char in template:
        if char not in countMap:
            countMap[char] = 0
        countMap[char] += 1

    for _ in range(insertions):
        newTemplateMap = templateMap.copy()
        removePairs = []
        for pair, occurance in templateMap.items():
            if occurance > 0 and pair in pairInsertions.keys():
                char = pairInsertions[pair]
                newTemplateMap[pair] -= occurance
                pair1 = pair[0]+char
                pair2 = char+pair[1]
                if pair1 not in newTemplateMap:
                    newTemplateMap[pair1] = 0
                if pair2 not in newTemplateMap:
                    newTemplateMap[pair2] = 0
                newTemplateMap[pair1] += occurance
                newTemplateMap[pair2] += occurance
                if char not in countMap:
                    countMap[char] = 0
                countMap[char] += occurance
        templateMap = newTemplateMap

    return max(countMap.values())-min(countMap.values())


print(findPolymerStrain("input.txt",10))
print(findPolymerStrain("input.txt",40))

