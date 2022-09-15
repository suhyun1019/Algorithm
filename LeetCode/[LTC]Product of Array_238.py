num=[1,2,3,4]
ans=[]
sum=1

for i in range(len(num)) :
    ans.append(sum)
    sum*=num[i]

sum=1
num.reverse()
for j in range(len(num)) :
    ans[len(num)-1-j]*=sum
    sum*=num[j]

print(ans)
