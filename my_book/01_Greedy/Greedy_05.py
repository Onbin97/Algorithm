# 1이 될 때까지

# 어떠한 수 N이 1이 될 때까지  다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
# 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

n, k = map(int, input().split())

# 내가 푼 풀이
a = 0
while True:
    if n % k == 0:
        n //= k
        a += 1
    else:
        n -= 1
        a += 1
    
    if n == 1:
        break
    
print(a)

# 정답

result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
    