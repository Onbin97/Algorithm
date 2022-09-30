# 약수의 개수와 덧셈

#내가 푼 풀이
def solution(left, right):
    nums = list(range(left, right+1))
    
    count = 0
    for i in nums:
        n = 1
        num_count = 0 
        while n <= i:
            if not i % n:
                num_count += 1
            n += 1
        
        if num_count % 2:
            count -= i
        else: 
            count += i    
    return count

print(solution(24, 27))

# 다른 풀이

def solution2(left, right):
    answer = 0 
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer
    
print(solution2(24, 27))
        