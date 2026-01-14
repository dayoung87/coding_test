# 2798 블랙잭
"""
    꼭 모든 경우의 수를 다 확인해봐야 하나? 다른 방법이 있을 것 같은데
    뭐 이것조차 오류나서 틀렸음
"""

n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = -1

for i in range(n):
    for j in range(i):
        for k in range(j):
            temp = cards[i] + cards[j] + cards[k]

            if(temp <= m):
                result = max(result, temp)

print(result)