
# 내가 푼 풀이
def solution(answers):
    a, b, c = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a *= len(answers)
    b *= len(answers)
    c *= len(answers)
    
    a_count, b_count, c_count = 0, 0, 0

    for x, y, z, answer in zip(a, b, c, answers):
        if x == answer:
            a_count += 1
        if y == answer:
            b_count += 1
        if z == answer:
            c_count += 1
    
    max_count = max(a_count, b_count, c_count)
    answer = []
    
    if max_count == a_count:
        answer.append(1)
    if max_count == b_count:
        answer.append(2)
    if max_count == c_count:
        answer.append(3)
    
    return answer


print(solution([1,3,2,4,2]))

# 다른 풀이
def solution2(answers):
    a, b, c = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    scores = [0, 0, 0]
    result = []
    
    for idx, answer in enumerate(answers):
        if answer == a[idx%len(a)]:
            scores[0] += 1
        if answer == b[idx%len(a)]:
            scores[1] += 1
        if answer == c[idx%len(a)]:
            scores[2] += 1
    
    for idx, score in enumerate(scores):
        if score == max(scores):
            result.append(idx+1)
    
    return result

print(solution2([1,3,2,4,2]))