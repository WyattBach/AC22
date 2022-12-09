with open('AC22/AC22input-8.txt') as f:
    data = [x.strip() for x in f.readlines()]

# data = [
#     '30373',
#     '25512',
#     '65332',
#     '33549',
#     '35390',
#         ]

ans = 0
for i in range(1,len(data)-1):
    for j in range(1,len(data[i])-1):
            tree = int(data[i][j])
            lscore,rscore,uscore,dscore, = 0,0,0,0
            #check left
            for k in reversed(data[i][:j]):
                lscore += 1
                if int(k) >= tree:
                    break

            #check right
            for k in data[i][j+1:]:
                rscore += 1
                if int(k) >= tree:
                    break

            #check up


            for k in reversed(data[:i]):
                uscore += 1
                if int(k[j]) >= tree:
                    break
                
            #check down
            for k in data[i+1:]:
                dscore += 1
                if int(k[j]) >= tree:
                    break

            if lscore * rscore * uscore * dscore > ans:
                ans = lscore * rscore * uscore * dscore
                print(uscore)

print(ans)