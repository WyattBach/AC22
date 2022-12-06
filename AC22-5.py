with open('AC22\AC22input-5.txt') as f:
    file = f.readlines()
    lines = [x.strip().split(' ') for x in file[10:]]
    stacks = [[] for i in range(9)]
    index = 0
    for i in range(8):
        for j in range(1,len(file[0]), 4):
            if file[i][j] != ' ':
                stacks[index].append(file[i][j])
            index += 1
        index = 0

for i in lines:
    amt = int(i[1])
    beg = int(i[3]) - 1
    des = int(i[5]) - 1
    for j in range(amt):
        stacks[des].insert(0,stacks[beg].pop(0))

ans = ''
for i in range(9):
    ans = ans + stacks[i][0]

print(ans)
