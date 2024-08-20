# solution1
def solution(s, n):
    answer = ''
    uplist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowlist = 'abcdefghijklmnopqrstuvwxyz'
    for i in s :
        if i.isupper() :
            answer+=uplist[(uplist.index(i)+n)%len(uplist)]
        elif i.islower() :
            answer+=lowlist[(lowlist.index(i)+n)%len(lowlist)]
        else :
            answer+=' '
    return answer

# solution2
def solution(s, n) :
    answer=''
    for i in s :
        if i.isupper() :
            answer+= chr((ord(i)+n)%23+ord('A'))
        elif i.islower() :
            answer+= chr((ord(i)+n)%23+ord('a'))
        else :
            answer+=i
    return answer
