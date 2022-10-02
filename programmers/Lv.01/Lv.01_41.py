# 숫자 문자열과 영단어

# 내가 푼 풀이
def solution(s):
    my_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for i in my_dict:
        s = s.replace(i, str(my_dict[i]))
    return int(s)

print(solution("one4seveneight"))

# 다른 풀이
# dictionary 아이템 메서드의 key, value를 활용한 풀이 
def solution2(s):
    my_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for key, value in my_dict.items():
        s = s.replace(key, str(value))
    return int(s)

print(solution2("one4seveneight"))