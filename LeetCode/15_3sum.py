num=[-1,0,1,2,-1,-4]

num.sort()
ans=[]

for i in range(len(num)-2) :
    right=len(num)-1
    left=i+1
    if num[i]==num[i-1] and i>0:
        continue
    while left<right :
        sum=num[i]+num[left]+num[right]

        if sum<0 :
            left+=1
        elif sum>0 :
            right-=1
        else :
            ans.append([num[i], num[left], num[right]])

            while left<right and num[left]==num[left+1] :
                left+=1
            while left<right and num[right]==num[right-1] :
                right-=1
            left+=1
            right-=1

print(ans)
