"""
시작: 3:40
종료: 3:54
"""
# 연산자 조합 경우 구하기
def dfs(v):

    if len(v)==n-1:
        operations.append(v[:])
        return

    for i in range(len(oper)):
        if oper[i]>0:
            v.append(i)
            oper[i]-=1
            dfs(v)
            v.pop()
            oper[i]+=1

n = int(input())
nums = list(map(int, input().split()))  # +,-,* 개수
oper = list(map(int, input().split()))
dic = {0:'+', 1:'-', 2:'*'}
operations = []
ans = []

dfs([])

for op in operations:
    s = nums[0]
    for i in range(n-1):
        s = eval(str(s)+dic[op[i]]+str(nums[i+1]))
    ans.append(s)

"""
for op in operations:
    s = nums[0]
    for i in range(n-1):
        if op[i]==0:
            s+=nums[i+1]
        elif op[i]==1:
            s-=nums[i+1]
        elif op[i]==2:
            s*=nums[i+1]
    ans.append(s)
"""
    
print(min(ans), max(ans))
