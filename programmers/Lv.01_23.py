# 내가 푼 풀이

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += (a[i] * b[i])
    return answer


print(solution([1,2,3,4,7], [-3,-1,0,2,7]))

# zip 을 활용한 다른 풀이

def solution2(a, b):
    return sum([x*y for x, y in zip(a, b)])

print(solution([1,2,3,4,7], [-3,-1,0,2,7]))
