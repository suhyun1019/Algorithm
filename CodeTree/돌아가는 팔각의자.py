table = [list(input()) for _ in range(4)]
n = int(input())
dic = {1:0, 2:0, 3:0, 4:0} # 테이블마다 12시의 의자를 나타내는 인덱스 

for i in range(n) :
    v,d = map(int, input().split())
    r, l = v, v
    while r<4 and table[r-1][(dic[r]+2)%8]!=table[r][(dic[r+1]-2)%8] :
        r+=1
    while l>1 and table[l-1][(dic[l]-2)%8]!=table[l-2][(dic[l-1]+2)%8] :
        l-=1
    
    # v(해당 의자)와 차이가 홀수이면 v와 반대방향으로 움직임, 차이가 짝수이면 v와 같은 방향으로 움직임  
    for j in range(l, r+1) :
        if abs(j-v)%2==1 :
            dic[j]+=d
        else :
            dic[j]+=d*(-1)

ans = 0
for k,v in dic.items() :
    ans+=2**(k-1)*int(table[k-1][v%8])
print(ans)
