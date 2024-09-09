def solution(n, stations, w):
    answer = (stations[0]-w-2)//(2*w+1)+1
    for i in range(len(stations)) :
        if i<len(stations)-1 :
            s, e = stations[i]+w+1, stations[i+1]-w-1
        else :
            s, e = stations[i]+w+1, n
            if s>n :
                break
        answer += (e-s)//(2*w+1)+1     
    
    return answer
