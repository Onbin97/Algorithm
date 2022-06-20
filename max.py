num_range = 9
num_lst = []

for num in range(0, num_range):
    num = int(input())
    num_lst.append(num)

maximum = max(num_lst)
idx = num_lst.index(maximum) + 1
print(maximum)
print(idx)