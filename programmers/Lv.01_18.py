
# 내가 푼 풀이
def solution(arr, divisor):
    answer = [i for i in arr if not i % divisor]
    if not len(answer):
        return [-1]
    answer.sort()
    return answer


print(solution([5, 9, 7, 10], 5))
print(solution([9, 7], 5))

# 다른 풀이

def solution2(arr, divisor):
    return sorted([i for i in arr if not i % divisor]) or [-1] 
    # 빈리스트는 False 이다. 따라서 False 값이 인식되어 or 로 빈배열일 경우를 대처할 수 있는 부분이다.

print(solution2([5, 9, 7, 10], 5))
print(solution2([9, 7], 5))