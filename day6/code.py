def readfile(filename):
    with open(filename) as file:
        return list(map(int,file.readlines()[0].split(',')))

def countFishes(filename,days):
    startFishes = readfile(filename)

    fishes = [0]*9
    for fish in startFishes:
        fishes[fish] += 1

    for _ in range(days):
        newFish = fishes.pop(0)
        fishes.append(newFish)
        fishes[6] += newFish

    return sum(fishes)


print(countFishes("input.txt",80))
print(countFishes("input.txt",256))