num = int(input())
a = num
result = 0

while True:
    b = a // 10
    c = a % 10
    d = (b + c)%10
    a = (c * 10) + d

    result += 1
    if  a == num:
        break

print(result)
        
    