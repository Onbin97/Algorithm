# 수박수박수박수박수

# 내가 푼 풀이
def solution(n):
    answer = ''
    for i in range(1, n+1):
        if i % 2:
            answer += '수'
        else:
            answer += '박'
    
    return answer


print(solution(1))


# 다른 풀이

def solution2(n):
    answer = '수박' * n
    return answer[:n]

print(solution2(5))