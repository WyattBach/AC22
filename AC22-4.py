with open('AC22\AC22input-4.txt') as f:
    input = [x.strip().split(',') for x in f.readlines()]



ans = 0
for i in range(len(input)):
    min1,max1 = input[i][0].split('-')
    min2,max2 = input[i][1].split('-')
    if int(min1) <= int(min2) and int(max1) >= int(max2) or int(min2) <= int(min1) and int(max2) >= int(max1):
        ans += 1


print(ans)