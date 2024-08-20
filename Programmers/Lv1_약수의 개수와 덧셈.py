def solution(left, right):
    answer = 0
    for i in range(left, right+1) :
        ans = len([k for k in range(1, i+1) if i%k==0])
        if ans%2 :
            answer-=i
        else :
            answer+=i
    return answer
