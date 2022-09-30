# 최대공약수와 최소공배수

def solution(n, m):
    gcd = max([i for i in range(1, min(n, m)+1) if not n % i and not m % i])
    return [gcd, (n*m)//gcd]