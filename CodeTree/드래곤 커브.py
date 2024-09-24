n = int(input())
total = set()
direction = {0:(0,1), 1:(-1,0), 2:(0,-1), 3:(1,0)}

for i in range(n) :
    x,y,d,g = map(int, input().split())
    dots = set([(x,y),(x+direction[d][0],y+direction[d][1])])
    total.add((x,y))
    total.add((x+direction[d][0],y+direction[d][1]))
    last = list(dots)[-1]

    while g>0 :
        temp = []
        for dot in dots :
            temp.append([dot[1], dot[0]*(-1)])
        dx, dy = last[0]-temp[-1][0], last[1]-temp[-1][1]
        dots.pop()
        for j in range(len(temp)-1, -1, -1) :
            dots.add((temp[j][0]+dx, temp[j][1]+dy))
            total.add((temp[j][0]+dx, temp[j][1]+dy))
        last = list(dots)[-1]
        g-=1

ans = 0
for t in total :
    if (t[0]+1,t[1]) in total and (t[0],t[1]+1) in total and (t[0]+1,t[1]+1) in total :
        ans+=1
print(ans)
