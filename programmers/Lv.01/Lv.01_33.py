# 3진법 뒤집기

def solution(n):
    ternary = ''
    
    while n >= 3:
        ternary += str(n % 3)
        n = n // 3
    ternary += str(n)
    answer = int(ternary, 3)
    return answer