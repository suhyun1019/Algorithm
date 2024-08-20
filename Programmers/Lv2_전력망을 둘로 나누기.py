from collections import defaultdict

# 완전 탐색 - dfs 
def dfs(v, visited, graph) :
    
    visited.append(v)
    for w in graph[v] :
        if w not in visited :
            dfs(w, visited, graph)
    return visited

def solution(n, wires):
    ans = 100
    graph = defaultdict(list)
    
    for wire in wires :     # graph 생성 
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    for wire in wires :     # 방문한 
        a,b = wire[0],wire[1]
        a_res = dfs(a, [b], graph)
        b_res = dfs(b, [a], graph)
        print(a_res, b_res)
        ans = min(ans, abs(len(a_res)-len(b_res)))
        
    return ans

## 추가 설명 https://suding88.tistory.com/133
