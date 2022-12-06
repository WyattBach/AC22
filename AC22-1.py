with open('AC22\AC22input-1.txt') as f:
    trash = []
    input = []
    for i in f:
        if i != '\n':
            trash.append(int(i.strip()))
        else:
            input.append(trash)
            trash = []

# input = [[1000,2000,3000], [4000], [5000,6000], [7000,8000,9000], [10000]]


check = 0
ans = 0
for i in input:
    check = sum(i)
    if check > ans:
        ans = check
    check = 0

print(ans)