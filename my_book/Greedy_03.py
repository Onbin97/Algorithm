
# 처음 내가 푼 풀이
n, m, k = map(int, input().split())
# 
# data = list(map(int, input().split())) 

data = [2, 4, 5, 4, 6]
data.sort()

a = 0

a += data[-2] * (m % k)
a += data[-1] * (k * (m // k))

# 18 + 15 + 8
print(a)

# 정답보고 다시 풀이 (접근은 얼추 맞았지만 예외사항이 부족했음.)

data.sort()

first = data[-1]
second = data[-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
# 나머지가 있다면 더하기
count += (m % (k + 1))

result = 0
result += (count) * first
result += (m - count) * second

print(result)