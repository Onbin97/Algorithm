# 폰켓몬

# 내가 푼 풀이
def solution(nums):
    if len(set(nums)) >= len(nums) / 2:
        return len(nums) / 2
    return len(set(nums))

print(solution([3,3,3,3,3,4]))

# 다른 풀이

def solution2(nums):
    return min(len(nums)/2, len(set(nums)))