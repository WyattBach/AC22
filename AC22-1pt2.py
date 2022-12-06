with open('C:\Code\AC22input-1.txt') as f:
    trash = []
    input = []
    for i in f:
        if i != '\n':
            trash.append(int(i.strip()))
        else:
            input.append(trash)
            trash = []

check = 0
ans = [0,0,0]
for i in input:
    check = sum(i)
    for j in range(3):
        if check > ans[j]:
            ans[j] = check
            break
        
    check = 0

print(sum(ans))