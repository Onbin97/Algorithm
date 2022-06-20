def getTotalPage(m, n):
    if m % n == 0:
        return int((m / n))
    else:
        return int((m / n) + 1)



m, n = map(int, input().split())

print(getTotalPage(m, n))

