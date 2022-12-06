with open('AC22\AC22input-3.txt') as f:
    input = [x.strip() for x in f]


# input = ['vJrwpWtwJgWrhcsFMMfFFhFp',
# 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
# 'PmmdzqPrVvPwwTWBwg']


ans = 0
for i in range(2,len(input),3):
    for j in range(len(input[i])):
        if input[i][j] in input[i-1] and input[i][j] in input[i-2]:
            if input[i][j].isupper():
                ans += ord(input[i][j]) - 38
            else:
                ans += ord(input[i][j]) - 96
            break
    continue

print(ans)


            