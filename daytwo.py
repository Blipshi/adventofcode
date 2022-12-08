score = 0

with open('daytwoinput.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
        if f[line].find("A"):
            score += 1