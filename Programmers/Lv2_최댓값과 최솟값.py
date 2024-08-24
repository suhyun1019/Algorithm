def solution(s):
    slist = list(map(int, s.split()))
    return str(min(slist))+" "+str(max(slist))
