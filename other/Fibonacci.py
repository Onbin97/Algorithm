# 메모화 전
count = 0
def f(n):
    global count
    count += 1
    
    if n == 1 or n == 2:
        return 1
    return f(n - 2) + f(n - 1)

# print(f(1))
# print(f(2))
# print(f(3))
# print(f(4))
# print(f(5))
# print(f(6))

# print(f(35))

# print(count)

# 메모화 후

memory = {1: 1, 2: 1}
def mf(n):
    if n in memory:
        return memory[n]
    
    output = mf(n - 2) + mf(n - 1)
    memory[n] = output
    return output


print(memory)
print(mf(1000))