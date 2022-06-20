
lst = []

for a in range(10):
    a = int(input())
    b = a % 42
    lst.append(b)
    
print(len(set(lst)))


