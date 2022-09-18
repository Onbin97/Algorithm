# 콜라츠 추축

def solution(num):
    count = 0
    while num != 1:
        if num % 2:
            num = (num * 3) + 1
            count += 1
                     
        if not num % 2:
            num //= 2
            count += 1
        
        if count == 500:
            return -1
        
    return count