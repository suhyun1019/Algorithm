"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, 
a list of travel times as directed edges times[i] = (ui, vi, wi), 
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. 
Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.

(example)
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        def dijkstra(node) :     #다익스트라 함수
            
            m, min_num = 100000, 0
            visited.append(node)  #방문한 노드에 대해 방문 표시
            
            if len(visited)==n :  #모든 노드를 방문하면 return 
                return 
            
            for time in times :
                if time[0]==node :                                    #해당 node와 인접한 node에 대해
                    if table[time[1]-1]>table[time[0]-1]+time[2] :    #table 값 update
                        table[time[1]-1]=table[time[0]-1]+time[2]     #node에 갈 수 있는 최소값 갱신
                        
            for t in range(len(table)) :          
                if (t+1) not in visited and m>table[t] :              #방문하지 않은 node중 최소값을 가지는 node 선택
                    m=table[t]
                    min_num=t+1
            
            dijkstra(min_num)
            
        visited=[]
        table=[sys.maxsize for _ in range(n)]
        table[k-1]=0
        
        dijkstra(k)
        
        if max(table)==sys.maxsize :
            return -1
        else :
            return max(table)

