with open('AC22/AC22input-10.txt') as f:
    lines = [x.strip() for x in f]

import math as m

CRT = [[' ' for j in range(40)] for k in range(6)]
X = 1
#begins in position '0' so it has to be -1 to work with code
cyc = -1
for i in lines:
    if i == 'noop':
        cyc += 1
        if X - 1 <= cyc % 40 <= X + 1:
            CRT[m.floor(cyc/40)][cyc%40] = '#'
        else:
            if cyc == 240:
                break
            CRT[m.floor(cyc/40)][cyc%40] = ' '
    else:
        val = int(i.split()[1])
        cyc += 1
        if X - 1 <= cyc % 40 <= X + 1:
            CRT[m.floor(cyc/40)][cyc%40] = '#'
        else:
            CRT[m.floor(cyc/40)][cyc%40] = ' '
        cyc += 1
        if X - 1 <= cyc % 40 <= X + 1:
            CRT[m.floor(cyc/40)][cyc%40] = '#'
        else:
            CRT[m.floor(cyc/40)][cyc%40] = ' '
        X += val

for i in range(6):
    print(''.join(CRT[i]))


        