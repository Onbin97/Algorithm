# 카카오 다트게임
import re

# YouTube 해설보고 이해
def solution(dartResult):
    #각 option에 맞는 값은 dictionary에 저장
    options = {'S' : '**1', 'D' : '**2', 'T' : '**3', '#': '*-1'}
    
    # 정규표현식을 사용하여 문자열 분할
    # S,D,T 가 있는지 그다음에 #, * 이 있는지, ?로 #, * 은 있을수도 있고 없을수도 있다고 저장 
    # 그다음 split으로 분할
    lst = re.sub('([SDT][#*]?)', '\g<1> ', dartResult).split(' ')[:-1]
    
    result = []
    for i in lst:
        for j in i:
            i = i.replace(j, options.get(j, j))
        if i[-1] == '*':
            i += '2'
            # 앞에 값이 있다면 그값도 두배 곱해줘야함.
            if result:
                result[-1] += '*2'
        result.append(i)
     
    # 문자열을 바로 계산 할 수 있도록 해주는 함수 eval   
    return sum([eval(i) for i in result])

print(solution('1S2D*3T'))