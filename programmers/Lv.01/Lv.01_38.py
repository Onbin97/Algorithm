# 최소 직사각형

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))