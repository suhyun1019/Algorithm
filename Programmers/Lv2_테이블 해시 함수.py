def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x:(x[col-1], -x[0]))
    for r in range(row_begin-1, row_end) :
        t = 0
        for i in range(len(data[0])) :
            t+=data[r][i]%(r+1)
        answer^=t
    return answer
