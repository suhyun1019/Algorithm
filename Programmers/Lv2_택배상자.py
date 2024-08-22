# 스택 사용 
def solution(order):
    answer = 0
    n = len(order)
    ts = []
    s = [i for i in range(n,0,-1)]
    i = 0
    while 1 :
        if s and s[-1]==order[i] :  # 컨테이너에서 가져감
            s.pop()
            i+=1
        elif ts and ts[-1]==order[i] :  #보조컨테이너에서 가져감
            ts.pop()
            i+=1
        else :          #택배순서랑 안맞아서 보조컨테이너로 이동 
            if s :
                ts.append(s.pop())
            else : 
                break
    return i

# 문제 풀이 https://suding88.tistory.com/137
