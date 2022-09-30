# 부족한 금액 계산

# 내가 푼 풀이
def solution(price, money, count):
    result = 0
    for i in range(1, count+1):
        result += price * i
    if (money - result) >= 0:
        return 0

    return abs(money - result)

print(solution(3, 20, 4))

# 다른 풀이
# min 함수로  0 과 비교하여 더 작은값을 도출해낸 후, 절대값으로 리턴한다.

def solution2(price, money, count):
    return abs(min(money - sum([price * i for i in range(1, count+1)]), 0))

print(solution2(3, 20, 4))