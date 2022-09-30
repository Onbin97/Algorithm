# [1차] 비밀지도

def solution(n, arr1, arr2):
    answer = []    
    for x, y in zip(arr1, arr2):
        s = ''
        for i, j in zip(f'{x:0{n}b}', f'{y:0{n}b}'):
            if int(i) or int(j):
                s += '#'
            else: s += ' '
        answer.append(s)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))