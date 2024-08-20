def solution(numbers):
    answer = []
    for num in numbers :
        bit = bin(num)[2:]
        if '0' in bit :
            t = bit[::-1].index('0')
            answer.append(num+2**t-int(2**(t-1)))
        else :
            answer.append(int('10'+bit[1:], 2))
    return answer
