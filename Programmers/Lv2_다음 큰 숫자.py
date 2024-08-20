def solution(n):
    cnt = bin(n).count('1')
    
    next_n = n+1
    while 1 :
        b = bin(next_n)
        if b.count('1') == cnt :
            return next_n
        next_n+=1
