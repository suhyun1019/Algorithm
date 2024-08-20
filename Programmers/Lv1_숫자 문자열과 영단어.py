def solution(string):
    answer = ''
    nums = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    s = ''
    for i in range(len(string)) :
        if string[i].isdigit() :
            answer+=string[i]
        else :
            s+=string[i]
            if s in nums :
                answer+=nums[s]
                s = ''
    return int(answer)

