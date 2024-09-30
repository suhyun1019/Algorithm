# DFS, BFS

import copy

n,m,d = map(int, input().split())
table = [list(map(int, input().split())) for _  in range(n)]
combination = []
com = [(n, i) for i in range(m)]
ans = 0
moves = [(0,-1),(-1,0),(0,1)]

# 조합 - 공격자 모든 좌표 경우 구하기
def comb(n, i, v, com) :

    if len(v)==3 :
        combination.append(v[:])
        return

    for c in range(i, len(com)) :
        if com[c] not in v :
            v.append(com[c])
            comb(n, c, v, com)
            v.pop()

comb(n, 0, [], com)

for combi in combination :
    cnt = 0
    temp = copy.deepcopy(table)
    # 공격 좌표 경우 하나
    while 1 :
        attack, s = [], 0
        for c in combi :
            q = [(c[0]-1, c[1])]
            visited = []
            check = 0   # 적 공격 여부
            while q :
                v=q.pop(0)
                visited.append(v)
                if temp[v[0]][v[1]]==1 :
                    check=1
                    break
                for move in moves :
                    dx,dy = v[0]+move[0], v[1]+move[1]
                    if 0<=dx<n and 0<=dy<m and (dx,dy) not in visited :
                        if abs(c[0]-dx)+abs(c[1]-dy)>d :
                            continue
                        q.append((dx,dy))

            if check :
                attack.append(v)

        # 한바퀴 끝: 공격 처리 -> 한칸씩 미루기
        cnt += len(list(set(attack)))   # 적 공격 회수 (중복 제거)

        for at in attack :
            temp[at[0]][at[1]]=0

        temp.pop()
        temp.insert(0, [0]*m)

        for i in range(n) :
            s+=temp[i].count(1)
        if s==0 : # 공격할 적이 없다면 
            ans = max(ans, cnt)
            break
print(ans)
