# lotto 최고순위와 최저순위
def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5}
    result = [i for i in lottos if i in win_nums]
    
    return [rank.get(len(result)+lottos.count(0), 6), rank.get(len(result), 6)]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))