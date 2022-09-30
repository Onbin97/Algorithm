# 정수 내림차순으로 배치하기

def solution(n):
    a = list(map(int, str(n)))
    a.sort()
    result = int(''.join([str(i) for i in a[::-1]]))
    return result