def solution(data, ext, val_ext, sort_by):
    dic = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    return sorted(list(d for d in data if d[dic[ext]]<val_ext), key=lambda d:d[dic[sort_by]])
