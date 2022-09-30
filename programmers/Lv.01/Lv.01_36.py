# 시저암호 


# 코드는 이해가 가지만 아직 처음부터 풀지는 못할 것 같음. (공부 더 필요)
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        # 대문자 체크
        if s[i].isupper():
            # 알파벳이 25글자이니 더 큰 수인 26으로 나머지 연산자를 이용하면, 
            # z의 경우처럼 맨 마지막이 다시 처음으로 돌아가는 경우의 수를 해결 할 수 있다.            
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
 
    return "".join(s)


