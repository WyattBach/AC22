with open('AC22\AC22input-3.txt') as f:
    input = [x.strip() for x in f]


ans = 0
for i in input:
    x = i[int(len(i)/2):]
    y = i[:int(len(i)/2)]
    for j in x:
        if j in y:
            if j.isupper():
                ans += ord(j) - 38
            else:
                ans += ord(j) - 96
            break
                
    continue

print(ans)
            



