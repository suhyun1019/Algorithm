def solution(arr, divisor):
    answer = [a for a in arr if a%divisor==0]
    answer.sort()
    return answer if answer else [-1]
