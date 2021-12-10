
def readfile(filename):
    with open(filename) as file:
        return [int(line.rstrip()) for line in file.readlines()]


def test(filename):
    lines = readfile(filename)
    return lines

print(test("input.txt"))

