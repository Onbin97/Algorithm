# 문자열 내림차순으로 배치하기


#내가 푼 풀이
def solution(s):
    return ''.join(sorted(list(s), reverse=True))

print(solution('Zbcdefg'))


# 다른 풀이
def solution2(s):
    return ''.join(sorted(s, reverse=True))

print(solution2('Zbcdefg'))
