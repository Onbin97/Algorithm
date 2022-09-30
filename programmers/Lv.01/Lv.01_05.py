# 정수 제곱근 판별

import math

def solution(n):
    a = math.sqrt(n)
    if (a % 1):
        return -1
    return (a+1)**2