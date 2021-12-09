
# PART 1

def readfile(filename):
    with open("input.txt") as file:
        lines = []
        for p1, p2 in [l.rstrip().split('|') for l in file.readlines()]:
            lines.append((p1.strip().split(),p2.strip().split()))
        return lines

def segment1(filename):
    lines = readfile(filename)
    count = 0
    for p1, p2 in lines:
        for digit in p2:
            if len(digit) in {2,3,4,7}:
                count += 1
    return count

print(segment1("input.txt"))

# PART 2

class Display:

    def __init__(self, filename):
        self.numbers_string = self._get_string_prefix(filename)
        self.configs = self._get_config()
        self.numbers = self._get_numbers()
        self.sum = self._get_sum(filename)

    def _get_string_prefix(self, filename):
        with open(filename) as file:
            return [l.strip().split('|')[0].strip() for l in file.readlines()]

    def _get_string_postfix(self, filename):
        with open(filename) as file:
            return [l.strip().split('|')[1].strip() for l in file.readlines()]

    def _sort_string(self, s):
        return ''.join(sorted(s))

    def _xor_string(self,s1,s2):
        s = ''
        if len(s2) > len(s1):
            s1,s2 = s2,s1
        for c in s1:
            if c not in s2:
                s += c
        return s

    def _get_config(self):
        configs = []
        letters = "abcdefg"
        for numbers in self.numbers_string:
            config = [' ']*7
            for letter in letters:
                count = numbers.count(letter)
                if count == 4:
                    config[4] = letter
                if count == 6:
                    config[1] = letter 
                if count == 9:
                    config[5] = letter
            one,four,seven,eight = '','','',''
            for number in numbers.split():
                numLen = len(number)
                if numLen == 2:
                    one = number
                if numLen == 4:
                    four = number
                if numLen == 3:
                    seven = number
                if numLen == 7:
                    eight = number
            config[0] = self._xor_string(one,seven)
            config[2] = self._xor_string(one,config[5])
            zero = ''
            for number in numbers.split():
                if len(number) == 6:
                    zero_mask = config[0]+config[1]+config[2]+config[4]+config[5]
                    char = self._xor_string(number,zero_mask)
                    if len(char) == 1:
                        config[6] = char
                        zero = number
                        break
            config[3] = self._xor_string(zero,eight)
            configs.append(config)
        return configs

    def _get_numbers(self):
        numbers = []
        for config in self.configs:
            number = ['']*10
            number[0] = self._sort_string(config[0]+config[1]+config[2]+config[4]+config[5]+config[6])
            number[1] = self._sort_string(config[2]+config[5])
            number[2] = self._sort_string(config[0]+config[2]+config[3]+config[4]+config[6])
            number[3] = self._sort_string(config[0]+config[2]+config[3]+config[5]+config[6])
            number[4] = self._sort_string(config[1]+config[2]+config[3]+config[5])
            number[5] = self._sort_string(config[0]+config[1]+config[3]+config[5]+config[6])
            number[6] = self._sort_string(config[0]+config[1]+config[3]+config[4]+config[5]+config[6])
            number[7] = self._sort_string(config[0]+config[2]+config[5])
            number[8] = self._sort_string(config[0]+config[1]+config[2]+config[3]+config[4]+config[5]+config[6])
            number[9] = self._sort_string(config[0]+config[1]+config[2]+config[3]+config[5]+config[6])
            numbers.append(number)
        return numbers

    def _get_sum(self,filename):
        numbers = self._get_string_postfix(filename)
        config = self.numbers
        total = 0
        for i, number in enumerate(numbers):
            d1,d2,d3,d4 = list(map(self._sort_string,number.split()))
            d1 = config[i].index(d1)
            d2 = config[i].index(d2)
            d3 = config[i].index(d3)
            d4 = config[i].index(d4)
            total += 1000*d1 + 100*d2 + 10*d3 + d4
        return total

def segment2(filename):
    display = Display(filename)
    return display.sum

print(segment2("input.txt"))

