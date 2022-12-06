with open('C:/Users/whata/.vscode/Advent of Code/AC22/AC22input-2.txt') as f:
    input = [x.strip() for x in f.readlines()]

#loss = x
#draw = y
#win = z
#rock = a
#paper = b
#scissors = c

ans = 0
for i in input:
    if i[2] == 'X':
        if i[0] == 'A':
            ans += 3
        elif i[0] == 'B':
            ans += 1
        elif i[0] =='C':
            ans += 2
    elif i[2] == 'Y':
        ans += 3
        if i[0] == 'A':
            ans += 1
        elif i[0] == 'B':
            ans += 2
        elif i[0] == 'C':
            ans += 3
    elif i[2] == 'Z':
        ans += 6
        if i[0] == 'A':
            ans += 2
        elif i[0] == 'B':
            ans += 3
        elif i[0] == 'C':
            ans += 1

print(ans)