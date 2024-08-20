def solution(sizes):
    w,h = 0,0
    for size in sizes :
        a,b = max(size), min(size)
        w,h = max(w,a), max(h,b)
    return w*h
