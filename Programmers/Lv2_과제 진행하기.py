def solution(plans):
    answer = []
    plan = [[p[0], int(p[1].split(':')[0])*60+int(p[1].split(':')[1]), int(p[2])] for p in plans]
    plan.sort(key=lambda x:-x[1])
    stack = []
    now = 0
    sec = 0
    
    while len(plan) or len(stack) :
        if plan and plan[-1][1]==sec :    # 새로운거 시작시간일때
            if now :                    # 현재 진행중인게 있다면 
                stack.append(now)
            now = plan.pop()
        if now :                      # 현재거 진행 
            now[2]-=1
            if now[2]<=0 :              # 종료 
                answer.append(now[0])
                now = 0
                sec-=1
        elif stack :                   # 진행할거 없고 이전것 가져오기
            now = stack.pop()
        sec+=1
        
    answer.append(now[0])
    return answer
