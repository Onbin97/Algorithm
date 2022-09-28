# 내가 푼 풀이
def solution(s):
    lst = s.split(' ')
    new_lst = []
    for i in lst:
        str_lst = []
        new_lst.append(str_lst)
        for j in range(len(i)):
            if not j % 2:
               str_lst.append(i[j].upper()) 
            else: str_lst.append(i[j].lower()) 
    
    ans = ' '.join([''.join(i) for i in new_lst])      
    return ans

print(solution('memo try hello world'))

# 다른 풀이
# 중첩 반복문보단 enumerate 를 활용하자.

def solution2(s):
    return ' '.join([''.join([y.lower() if x % 2 else y.upper() for x, y in enumerate(i)]) for i in s.split(' ')])
    
    
print(solution2('memo try hello world'))