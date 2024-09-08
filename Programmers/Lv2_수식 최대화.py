import re

def solution(expression):
    answer = 0
    ranks = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','+','-'],['*','-','+']]
    nums = re.sub('\D', ' ', expression).split()
    opers = re.sub('\d', ' ', expression).split()
    
    for rank in ranks :
        num_copy = nums.copy()
        oper_copy = opers.copy()
        for r in rank :
            i = 0
            while i<len(oper_copy) :
                if oper_copy[i] == r :
                    num_copy[i] = str(eval(num_copy[i]+r+num_copy[i+1]))
                    num_copy.pop(i+1)
                    #oper_copy.pop(i)
                else :
                    i+=1
        answer = max(answer, abs(int(num_copy[0])))
    return answer
