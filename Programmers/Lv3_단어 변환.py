def solution(begin, target, words):
    cnt = 0
    if target not in words :
        return 0
    words.sort()
    
    while target!=begin :
        for word in words :
            chk = 1
            for i in range(len(word)) :
                if word[i]!=begin[i] :
                    chk-=1
                if chk<0 :
                    break
            if chk==0 :
                cnt+=1
                begin=word
                words.remove(word)
                break
                
    return cnt
