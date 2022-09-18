# 하샤드 수

def solution(x):
    lst = list(map(int, str(x)))
    return not (x % sum(lst))