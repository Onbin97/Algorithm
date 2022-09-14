# 숫자 카드 게임

# 숫자가 쓰인 카드들 중 행을 기준으로 가장 작은 수의 카드를 고르고, 그 중에서 가장 큰 수의 카드를 찾는다.

n, m  = map(int, input().split())
    
data = [min(list(map(int, input().split()))) for i in range(n)]

print(max(data)) # 카드를 구하는 식
print(data.index(max(data))+1) # 행을 구하는 식
