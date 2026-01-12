# 1978 소수 찾기
"""
    2부터 시작해서 숫자의 제곱근까지 반복해서 나눔.
    1은 소수가 아님. 
    나머지가 0인 경우가 1번이라도 있다면 소수 아님.
"""
import math

n = int(input())
cnt = 0

num = list(map(int, input().split()))
for i in num:

    if i == 1:
        continue
    
    else:
        for k in range(2, math.floor(math.sqrt(i))):
            if(i % k == 0):
                continue
            else:
                cnt += 1

print(cnt)