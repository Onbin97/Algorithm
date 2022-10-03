# 소수 찾기

# 에라토스테네스의 체
def solution(n):
    nums = set(range(2, n+1))
    
    for i in range(2, n+1):
        nums -= set(range(2*i, n+1, i))
            
    return len(nums)

print(solution(10000))