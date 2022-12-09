with open('AC22/AC22input-9.txt') as f:
    data = [x.strip() for x in f]

vis = set()
rope = [[0,0] for x in range(10)] 

def radj(H,T):
    if abs(H[1] - T[1]) > 1 or abs(H[0] - T[0]) > 1:
            if H[1] < T[1]:
                T[1] -= 1
            elif H[1] > T[1]:
                T[1] += 1
            if  H[0]< T[0]:
                T[0] -= 1
            elif H[0] > T[0]:
                T[0] += 1
    return(T)

hx,hy = 0,0
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
        rope[0] = [hy,hx]
        for k in range(1,len(rope)):
            T = radj(rope[k-1], rope[k])
            rope[k] = T
        
        vis.add(tuple(rope[9]))

print(len(vis))
