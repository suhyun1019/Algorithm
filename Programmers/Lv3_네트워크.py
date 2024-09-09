from collections import defaultdict

# dfs - 재귀
def dfs(n, visited, graph) :
    
    for g in graph[n] :
        if g not in visited :
            visited.append(g)
            visited = dfs(g, visited, graph)
    return visited
    
def solution(n, computers):
    answer = 0
    graph = defaultdict(list)
    for i,computer in enumerate(computers) :
        for j,c in enumerate(computer) :
            if c==1 and i!=j:
                graph[i].append(j)

    v = []
    for i in range(len(computers)) :
        if i not in v :
            v+=dfs(i, [], graph)
            answer+=1
            
    return answer

#############################################
# dfs - 스택
def solution(n, computers) :
    answer = 0
    graph = defaultdict(list)
    for i,computer in enumerate(computers) :
        for j,c in enumerate(computer) :
            if c==1 and i!=j:
                graph[i].append(j)
        
    visited = []
    for i in range(len(computers)) :
        if i not in visited :
            stack = [i]
            while stack :
                n = stack.pop()
                for g in graph[n] :
                    if g not in visited :
                        visited.append(g)
                        stack.append(g)
            answer+=1
    return answer
