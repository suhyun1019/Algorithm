def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    plus = sum(month[:a-1])+b
    return day[plus%7]
