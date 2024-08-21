from collections import Counter 

# 카운터 사용 (카운터 교집합, elements 함수 사용)
def solution(X, Y):
    ans = sorted((Counter(X)&Counter(Y)).elements(), reverse=True)
    
    if len(ans)==0 :
        return '-1'
    elif ans[0]=='0' :
        return '0'
    else :
        return ''.join(ans)
