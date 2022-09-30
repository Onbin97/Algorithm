# 자연수 뒤집어 배열로 만들기


#내가 푼 풀이
def solution(n):
    a = str(n)
    lst = [int(a[i]) for i in range(len(a))][::-1]
    
    return lst

# 다른 사람이 푼 풀이

def any_solution(n):
    lst = list(map(int, reversed(str(n))))
    return lst