# 체육복

# 내가 푼 풀이
def solution(n, lost, reserve):
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)
    for i in reserve_only:
        
        if i - 1 in lost_only:
            lost_only.remove(i - 1)
        elif i + 1 in lost_only:
            lost_only.remove(i + 1)
    
    return n  - len(lost_only)

print(solution(5, [2, 3, 4], [1, 3, 5]))