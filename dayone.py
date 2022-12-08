elves= []
sum = 0

with open('dayoneinput.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
        if line != "":
            sum += int(line)
        else:
            elves.append(sum)
            sum = 0

max_cal = 0
elves.sort()
elves.reverse()
max_cal = elves[0] + elves[1] + elves[2]
print(max_cal)
