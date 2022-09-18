# 음양 더하기

def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if not signs[i]:
            absolutes[i] -= (absolutes[i] * 2)
    return sum(absolutes)


print(solution([4,7, 12], [True, False, True]))