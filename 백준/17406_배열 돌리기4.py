# dfs, 구현(회전)

import copy

n,m,k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
rotation = [list(map(int, input().split())) for _ in range(k)]
perm = []
ans = 5000

def permutation(v) :

    if len(v)==k :
        perm.append(v[:])
        return

    for i in range(k) :
        if i not in v :
            v.append(i)
            permutation(v)
            v.pop()

# (x-k, y-k) ~ (x+k, y+k)
def rotate(x,y,k, table) :

    if k<1 :
        return

    temp = table[x-k][y-k]
    for dx in range(x-k, x+k) :
        table[dx][y-k] = table[dx+1][y-k]
    for dy in range(y-k, y+k) :
        table[x+k][dy] = table[x+k][dy+1]
    for dx in range(x+k, x-k, -1) :
        table[dx][y+k] = table[dx-1][y+k]
    for dy in range(y+k, y-k, -1) :
        table[x-k][dy] = table[x-k][dy-1]
    table[x-k][y-k+1] = temp
    rotate(x, y, k-1, table)

permutation([])
# 모든 회전 경우에 대해
for pm in perm :
    temp = copy.deepcopy(table)
    for p in pm :
        r = rotation[p]
        rotate(r[0]-1, r[1]-1, r[2], temp)
    s = 5000
    for i in range(n) :
        s = min(s, sum(temp[i]))
    ans = min(ans, s)
print(ans)
