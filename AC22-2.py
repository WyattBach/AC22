with open('C:/Users/whata/.vscode/Advent of Code/AC22/AC22input-2.txt') as f:
    input = [x.strip() for x in f.readlines()]

#rock = a or x
#paper = b or y
#scissors = c or z
ans = 0
for i in input:
    if i[2] == 'X':
        ans += 1
        if i[0] == 'A':
            ans += 3
        elif i[0] == 'C':
            ans += 6
    elif i[2] == 'Y':
        ans += 2
        if i[0] == 'A':
            ans += 6
        elif i[0] == 'B':
            ans += 3
    elif i[2] == 'Z':
        ans += 3
        if i[0] == 'B':
            ans += 6
        elif i[0] == 'C':
            ans += 3

print(ans)
    