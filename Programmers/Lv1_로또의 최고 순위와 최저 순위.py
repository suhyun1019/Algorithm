def solution(lottos, win_nums):
    b = len(set(lottos)&set(win_nums))  # 원래 일치하는 최소 원소들
    a = b+lottos.count(0)               # 일치하게 만들수있는 
    return [min(7-a,6),min(7-b,6)]
