with open('dayfourinput.txt', encoding='utf-8') as f:
    sum = 0
    for line in f:
        line = line.strip('\n')
        line = line.split(",")
        
        elf1 = line[0].split("-")
        elf2 =  line[1].split("-")
        
        elf1[0] = int(elf1[0])
        elf1[1] = int(elf1[1])
        elf2[0] = int(elf2[0])
        elf2[1] = int(elf2[1])
        
        total1 = elf1[0] >= elf2[0] and elf1[1] <= elf2[1]
        total2 = elf2[0] >= elf1[0] and elf2[1] <= elf1[1]
        partial1 = elf1[1] >= elf2[0] and elf1[0] < elf2[0]
        partial2 = elf2[1] >= elf1[0] and elf2[0] < elf1[0]
        
        
        if total1 or total2 or partial1 or partial2:
            sum+=1

print(sum)
        
        
    