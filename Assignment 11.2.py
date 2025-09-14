import re
hand = open('regex_sum_2155534.txt')
numlist = list()
total = 0
for line in hand:
    line = line.rstrip()
    numb = re.findall('[0-9]+', line)
    for num in numb:
        total = total + int(num)

print(total)