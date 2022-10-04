# 완주하지 못한 선수

# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 처음 내가 푼 풀이 (오답)
# 원래 풀었던 방식에서 효울성 부적합이 나왔기 때문에 시도한 코드
# 모든 참가자 선수마다 dictionary로 번호를 지정해준뒤 참가자번호의 합과 완주자 번호의 합을 뺀 번호가 완주하지 못한 선수라고 생각
# 하지만 hash 개념을 활용한 접근방식은 문제의도에 맞았음
def solution(participant, completion):
    my = {}
    for i in range(len(participant)):
        my[participant[i]] = i + 1
    reversed_my = {y : x for x, y in my.items()}
    if not reversed_my.get(sum(my.values()) - sum([my[i] for i in completion])):
        for a in participant:
            if participant.count(a) == 2:
                return a 
        
    return reversed_my.get(sum(my.values()) - sum([my[i] for i in completion]))
        
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

#제대로된 hash 함수를 통한 구현.
def solution2(participant, completion):
    hash_dict = {}
    sum_hash = 0
    for part in participant:
        hash_dict[hash(part)] = part 
        sum_hash += hash(part)
    for comp in completion:
        sum_hash -= hash(comp)
     
    return hash_dict[sum_hash]
    
        
print(solution2(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

#단순한 Sort 와 Loop만으로도 풀 수 있음.
def solution3(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
    
    
print(solution3(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

# Counter를 활용한 구현
from collections import Counter
def solution4(participant, completion):
    part_counter = Counter(participant)
    comp_counter = Counter(completion)
    
    answer = part_counter - comp_counter
    
    return list(answer.keys())[0]

print(solution4(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))