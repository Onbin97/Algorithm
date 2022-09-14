lst = [1, 1, 3, 4, 5, 7, 8, 9, 10, 11]

nums_set = set(lst)
result = 0

for num in nums_set:
    if (num - 1) not in nums_set:
        length = 0
        while (num + length) in nums_set:
            length += 1
        
        result = max(result, length)
        
print(result)
            
