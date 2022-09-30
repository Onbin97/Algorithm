# 문자열 내 마음대로 정렬하기

# sort 활용법 찾아보다가 힌트를 얻었다.
def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x))
    
    return strings

print(solution(["sun", "bed", "car"], 1))