def makeCrates(num):
    crates = {}
    for i in range(num):
        crates[i+1] = []
    return crates
        

def getCrates(data):
    temp = []
    crates = makeCrates(9)
    for row in data:
        if row == " 1   2   3   4   5   6   7   8   9 ":
            break
        else:
            temp.append(row)
            
    temp.reverse()
    
    for row in temp:
        col = 1
        chars = list(row)
        for i in range (1, len(chars), 4):
            c = chars[i]
            if c.upper() != c.lower():
                crates[col].append(c)
            col += 1
            if col == 10:
                col = 1
    return crates
    
data = []
with open('dayfiveinput.txt', encoding='utf-8') as f:
    for line in f:
        data.append(line.strip("\n"))
crates = getCrates(data)
print(crates)