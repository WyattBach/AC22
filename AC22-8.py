with open('AC22/AC22input-8.txt') as f:
    data = [x.strip() for x in f.readlines()]

# data = [
#     '30373',
#     '25512',
#     '65332',
#     '33549',
#     '35390',
        # ]


ans = 0

for i in range(1,len(data)-1):
    for j in range(1,len(data[i])-1):
        tree = int(data[i][j])
        check = 0
        #check left
        for k in data[i][:j]:
            if int(k) >= tree:
                check += 1
                break
        
        #check right
        for k in data[i][j+1:]:
            if int(k) >= tree:
                check += 1
                break

        #check up
        for k in data[:i]:
            if int(k[j]) >= tree:
                check += 1
                break
            
        #check down
        for k in data[i+1:]:
            if int(k[j]) >= tree:
                check += 1
                break
        if check < 4:
            # print(data[i][j], i, j)
            ans += 1

ans +=  2 *len(data)
ans += 2 *len(data[0])
ans -= 4


print(ans)