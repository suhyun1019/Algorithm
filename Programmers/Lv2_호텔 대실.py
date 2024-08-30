def solution(book_time):
    
    for i,bt in enumerate(book_time) :
        book_time[i] = [int((bt[0].split(':'))[0])*60+int((bt[0].split(':'))[1]), int((bt[1].split(':'))[0])*60+int((bt[1].split(':'))[1])]
    
    book_time.sort(key=lambda x:x[0])
    
    res = [[book_time.pop(0)]]
    for bt in book_time :
        for i in range(len(res)) :
            if res[i][-1][1]+10<=bt[0] :
                res[i].append(bt)
                break
            if i==len(res)-1 :
                res.append([bt])
    #print(res, len(res))
    return len(res)
