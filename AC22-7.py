with open('AC22/AC22input-7.txt') as f:
    input = [x.strip() for x in f]


# input = ['$ cd /',
#         '$ ls',
#         'dir a',
#         '14848514 b.txt',
#         '8504156 c.dat',
#         'dir d',
#         '$ cd a',
#         '$ ls',
#         'dir e',
#         '29116 f',
#         '2557 g',
#         '62596 h.lst',
#         '$ cd e',
#         '$ ls',
#         '584 i',
#         '$ cd ..',
#         '$ cd ..',
#         '$ cd d',
#         '$ ls',
#         '4060174 j',
#         '8033020 d.log',
#         '5626152 d.ext',
#         '7214296 k' 
#                 ]


dirdict = {}
cd = []
cdpath = []
for i in input:
    cmd = i.split()
    if cmd[1] == 'cd':
        if cmd[2] == '..':
            cdpath.pop()
        else:
            cdpath.append(cmd[2])
    elif cmd[1] == 'ls':
        continue
    else:
        try:
            size = int(cmd[0])
            for j in range(1,len(cdpath) + 1):
                key = ','.join(cdpath[:j])
                if key in dirdict:
                    dirdict[key] += size
                else:
                    dirdict[key] = size
        except:
            pass


ans = 0
for k in dirdict.values():
    if k <= 100000:
        ans += k
print(ans)


