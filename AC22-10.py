with open('AC22/AC22input-10.txt') as f:
    lines = [x.strip() for x in f]

# lines = [
#     'noop',
#     'addx 3',
#     'addx -5'
# ]
X = 1
cyc = 0
ans = 0
for i in lines:
    if i == 'noop':
        cyc += 1
        if cyc in [20, 60, 100, 140, 180, 220]:
            ans += cyc * X
    else:
        val = int(i.split()[1])
        cyc += 1
        if cyc in [20, 60, 100, 140, 180, 220]:
            ans += cyc * X
        cyc += 1
        if cyc in [20, 60, 100, 140, 180, 220]:
            ans += cyc * X
        X += val

print(ans)

        


        
        
