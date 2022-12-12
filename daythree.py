def getVal(c):
    val = 0 
    if c.islower():
        val = ord(c) - 96
    else:
        val = ord(c) - 38
    return val

packs = []

with open('daythreeinput.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
        packs.append(line)
        
    total = 0
    for pack in packs:
        half = len(pack)//2
        comp1 = pack[:half]
        comp2 = pack[half:]
        for item in comp1:
            if item in comp2:
                total += getVal(item)
                break
print(total)

total = 0 
length = len(packs)
for i in range(0, length, 3):
      pack1 = packs[i]
      pack2 = packs[i + 1]
      pack3 = packs[i + 2]
      for item in pack1:
          if item in pack2 and item in pack3:
              total += getVal(item)
              break
          
print(total)