# 2016년 요일 구하기

from datetime import date

def solution(a, b):
    weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return weekdays[date(2016, a, b).weekday()]

print(solution(5, 24))