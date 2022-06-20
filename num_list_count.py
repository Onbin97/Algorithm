A = int(input())
B = int(input())
C = int(input())

num_lst = list(str(A * B * C))

for i in range(10):
    print(num_lst.count(str(i)))
