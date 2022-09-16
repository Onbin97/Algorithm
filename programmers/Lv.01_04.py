# 약수의 합

def solution(n):
    a = 1
    answer = 0
    while a <= n:
        if not (n % a):
            answer += a
        a += 1
    return answer