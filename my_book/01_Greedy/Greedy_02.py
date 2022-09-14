m, k = map(int, input().split())

# data = list(map(int, input().split())) 

data = [2, 4, 5, 4, 6]
data.sort()
a = 0

while True:
    if m < k:
        a += data.pop(-1) * m
        m -= m
    if m == 0:
        break
    
    a += data.pop(-1) * k
    m -= k


# 18 + 15 + 8
print(a)