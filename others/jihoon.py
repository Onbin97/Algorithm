lst = [1, 2, 3, 5, 6, 7, 8]

nums_set = set(lst)
result = 0

for num in nums_set:
    if (num - 1) not in nums_set:
        length = 0
        while (num + length) in nums_set:
            length += 1
        
        result = max(result, length)
        
print(result)
            
