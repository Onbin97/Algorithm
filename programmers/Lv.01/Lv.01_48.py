# 실패율

# 내가 푼 풀이
def solution(N, stages):
    lst = []
    answer = []
    for i in range(1, N+1):
        if stages.count(i):
            lst.append(stages.count(i) / len(stages))
            stages = [j for j in stages if j not in {i}]
        else:
            lst.append(0)
    
    # print(lst.index(max(lst)))
    while sum(lst) != (-1 * len(lst)):
        answer.append(lst.index(max(lst))+1)
        lst[lst.index(max(lst))] = -1
            
    return answer

print(solution(4, [4,4,4,4,4]))

# 다른 풀이
def solution2(N, stages):
    result = {}
    users = len(stages)
    for stage in range(1, N+1):
        if users:
            count = stages.count(stage)
            result[stage] = count / users
            users -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

print(solution2(4, [4,4,4,4,4]))
