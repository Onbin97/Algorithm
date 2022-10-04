# 소수 만들기

# 내가 푼 풀이
def solution(nums):
    num_lst = []
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            for k in range(j + 1,len(nums)):
                num_lst.append(nums[i] + nums[j] + nums[k])
    # print(num_lst)           
    ns = set(range(2, max(num_lst) + 1))
    
    for i in range(2, max(num_lst) + 1):
        ns -= set(range(2*i, max(num_lst) + 1, i))
        
    return len([i for i in num_lst if i in ns])


print(solution([1,2,7,6,4]))

# 다른 풀이 (combinations 활용)

from itertools import combinations

def solution2(nums):
    num_lst = [sum(i) for i in combinations(nums, 3)]
    
    ns = set(range(2, max(num_lst) + 1))

    for i in range(2, max(num_lst) + 1):
        ns -= set(range(2*i, max(num_lst) + 1, i))
    
    return len([i for i in num_lst if i in ns])

print(solution2([1,2,7,6,4]))