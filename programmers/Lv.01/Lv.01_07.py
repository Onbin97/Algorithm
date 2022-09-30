# 문자열 내 p와 y의 개수

def solution(s):
    low = s.lower()
    return low.count('p') == low.count('y')

print(solution('PopoyY'))
