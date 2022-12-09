with open('AC22/AC22input-9.txt') as f:
    data = [x.strip() for x in f]


vis = set([0,0])
hx,hy= 0,0
tx,ty = 0,0
for i in data:
    dir,val = i.split()
    for j in range(int(val)):
        if dir == 'L':
            hx -= 1
        elif dir == 'R':
            hx += 1
        elif dir == 'U':
            hy += 1
        else:
            hy -= 1
        if abs(hx - tx) > 1 or abs(hy - ty) > 1:
            if hx < tx:
                tx -= 1
            elif hx > tx:
                tx += 1
            if hy < ty:
                ty -= 1
            elif hy > ty:
                ty += 1
            vis.add(tuple([ty,tx]))

print(len(vis))


                
