with open('AC22/AC22input-6.txt') as f:
    input = f.readline().strip()

for i in range(3,len(input)):
    check = 0
    pack = [input[i - j] for j in range(1,15)]
    for j in pack:
        if pack.count(j) > 1:
            check += 1
    if check == 0:
        print(i)
        break



    