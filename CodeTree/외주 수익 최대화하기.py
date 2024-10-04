n = int(input())
working = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def dfs(start, end, total):
    
    for i,w in enumerate(working):
        s,e = i,i+w[0]
        if end<=s and e<=n:
            dfs(s, e, total+w[1])

    price_list.append(total)

for i,w in enumerate(working):
    price_list = []
    s,e = i,i+w[0]
    if e<=n:
        dfs(s,e,w[1])
        ans = max(max(price_list), ans)
print(ans)
