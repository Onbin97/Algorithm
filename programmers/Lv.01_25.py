# 문자열 다루기 기본

#ㅓ 내가 푼 풀이
def solution(s):
    try:
        if len(s) != 4 and len(s) != 6:
            return False
        if int(s):
            return True
    except ValueError:
        return False

print(solution('111111'))

# 다른 풀이
def solution2(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    
    else:
        return False

print(solution2('111111'))

# 다른 풀이 2
def solution3(s):
    return s.isdigit() and len(s) in (4, 6)

# 다른 풀이 3
def solution4(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6