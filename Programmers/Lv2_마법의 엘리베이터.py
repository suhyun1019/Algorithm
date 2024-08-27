# 그리디 
def solution(storey):
    cnt = 0
    
    while storey :
        if storey%10 == 5 :     # 5일때 
            if (storey//10)%10>=5 : # 다음 숫자가 5이상이면 더하는게 이득 
                storey+=10
            cnt+=5
        elif storey%10>5 :      # 5이상이면 더하는게 이득 
            storey+=10
            cnt += (10-storey%10)
        else :                  # 5이하이면 빼는게 이득 
            cnt += storey%10
        storey //= 10
    return cnt
