score = 0
moves = []

with open('daytwoinput.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
        round = line.split(" ")
        moves.append(round)
        
for round in moves:
    if round[0] == "A": #opp = rock
        if round[1] == "X": #lose
            score += 0 + 3
        elif round[1] == "Y": #draw
            score += 3 + 1
        elif round[1] ==  "Z": #win
            score += 6 + 2
            
    elif round[0] == "B": #opp = paper
        if round[1] == "X":
            score += 0 + 1
        elif round[1] == "Y":
            score += 3 + 2
        elif round[1] ==  "Z":
            score += 6 + 3
    
    elif round[0] == "C": #opp = scissors
        if round[1] == "X":
            score += 0 + 2
        elif round[1] == "Y":
            score += 3 + 3
        elif round[1] ==  "Z":
            score += 6 + 1

print(score)