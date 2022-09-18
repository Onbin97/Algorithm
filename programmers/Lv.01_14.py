# 두 정수 사이의 합 

# 내가 푼 풀이
def solution(a, b):
    result = 0
    if a < b:
        while a < b:
            result += a
            a += 1
        return result + b
    
    if a > b:
        while b < a:
            result += b
            b += 1
        return result + b
    
    return a
        
# 다른 풀이 1

def solution2(a, b):
    if a == b: 
        return a
    
    if a > b: a, b = b, a
    
    return sum(range(a, b+1))

# 다른 풀이 2

def solution3(a, b):
    return (abs(a-b) + 1) * (a+b)//2