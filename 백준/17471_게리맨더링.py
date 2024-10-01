def bfs(nodes, graph):
    # 해당 리스트가 연결되어 있는지 확인
    q = [nodes[0]]
    visited = [nodes[0]]
    nodes.pop(0)
    while q:
        v = q.pop(0)
        if len(nodes)<1:
            return True
        for g in graph[v]:
            if g not in visited and g in nodes:
                visited.append(g)
                q.append(g)
                nodes.remove(g)
    if nodes :
        return False
    else :
        return True

def combination(num, v):

    if v:
        comb.append(v[:])
    if len(v)==num:
        return

    for i in range(n):
        if i not in v :
            v.append(i)
            combination(num, v)
            v.pop()
    return

n = int(input())
people_num = list(map(int, input().split()))
graph = {}
for i in range(n):
    graph[i] = list(map(int, input().split()))[1:]
    for j in range(len(graph[i])):
        graph[i][j]-=1

comb = []
combination(n//2, [])
people = set(i for i in range(n))
ans = 10000

for c in comb:
    red_sum,res = 0, 10000
    red, blue = c, list(people-set(c))
    if bfs(red[:], graph) and bfs(blue[:], graph):
        for i in range(n):
            if i in red:
                red_sum+=people_num[i]
        res = abs(sum(people_num)-red_sum-red_sum)
    ans = min(ans, res)

if ans==10000:
    print(-1)
else :
    print(ans)
