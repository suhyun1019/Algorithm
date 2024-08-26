def solution(k, score):
    top, res = [], []
    m = 2001
    for i,s in enumerate(score) :
        if i<k :
            m = min(s, m)
            top.append(s)
            res.append(m)
        else :
            if m<s :
                top.remove(m)
                top.append(s)
                m = min(top)
            res.append(m)
    return res
