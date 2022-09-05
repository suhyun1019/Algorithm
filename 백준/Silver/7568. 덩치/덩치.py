n=int(input())
weight=[]
height=[]
pos=[]

for w in range(n) :
    st=list(map(int, input().split()))
    weight.append(st[0])
    height.append(st[1])

for w in range(n) :
    pos.append(0)
    for u in range(n) :
        if w==u :
            continue
        if weight[w]<weight[u] and height[w]<height[u] :
            pos[w]+=1

    print(pos[w]+1, end=' ')