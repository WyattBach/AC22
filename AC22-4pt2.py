with open('AC22\AC22input-4.txt') as f:
    input = [x.strip().split(',') for x in f.readlines()]

ans = 0
for i in input:
    min1,max1 = i[0].split('-')
    min2,max2 = i[1].split('-')
    min1,min2,max1,max2 = int(min1),int(min2),int(max1),int(max2)
    if max1 >= min2 and min1 <= max2:
        ans += 1

print(ans)