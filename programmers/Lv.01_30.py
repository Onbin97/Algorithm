# 최대공약수와 최소공배수

def solution(n, m):
    gcd = max([i for i in range(1, min(n, m)+1) if not n % i and not m % i])
    return [gcd, (n*m)//gcd]


print(solution(2, 5))


# python 3.9 부터 사용 가능한 math library 활용
import math
def solution2(n, m):
    return [math.gcd(n, m), math.lcm(n, m)]
    
print(solution2(2, 5))