def getVal(c):
    val = 0 
    if c.islower():
        val = ord(c) - 96
    else:
        val = ord(c) - 38
    return val

packs = []

with open('daytwoinput.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
    total = 0
    for pack in packs: