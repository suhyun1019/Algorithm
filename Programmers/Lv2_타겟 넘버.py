# 10/30 7:37 ~ 7:47
# DFS
def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(num, idx):
        global answer
        
        if idx==len(numbers):
            if num==target:
                answer+=1
            return
        
        dfs(num+numbers[idx], idx+1)
        dfs(num-numbers[idx], idx+1)
        return
    
    dfs(0, 0)
    return answer
