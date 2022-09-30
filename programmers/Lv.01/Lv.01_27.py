# 행렬의 덧셈

def solution(arr1, arr2):
    answer = [[x + y for x, y in zip(i[0], i[1])] for i in zip(arr1, arr2)]
    return answer



a = [[1,2],[2,3]]
b = [[3,4],[5,6]]

print(solution(a, b))
print(solution([[1], [2]], [[3], [4]]))