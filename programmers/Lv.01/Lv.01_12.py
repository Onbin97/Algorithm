# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer =  [(x * i) for i in range(1, n+1)]
    return answer
