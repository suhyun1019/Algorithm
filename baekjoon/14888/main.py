from itertools import permutations

n=int(input())
slist=list(map(int, input().split()))
olist=list(map(int, input().split()))
op=['+','-','*','/']
oplist=[]

for i in range(4) :
    for j in range(olist[i]) :
        oplist.append(op[i])

oplist=list(set(permutations(oplist, n-1)))
max=-1000000000
min=1000000000

for i in oplist :
    res=slist[0]
    for j in range(len(slist)-1) :
        if i[j]=='+' :
            res+=slist[j+1]
        elif i[j]=='-' :
            res-=slist[j+1]
        elif i[j]=='*' :
            res*=slist[j+1]
        elif i[j]=='/' :
            if res>=0 :
                res//=slist[j+1]
            else :
                res=(-res)//slist[j + 1]
                res*=-1

    if res>max :
        max=res
    if res<min :
        min=res

print(max)
print(min)