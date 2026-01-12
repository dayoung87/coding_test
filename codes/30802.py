# 30802 웰컴 키트
"""
    input을 리스트로 받기, 숫자 올림 함수 ceil() 이용
    ceil()의 존재는 알고 있었는데 math 라이브러리라는 건 기억 못했음
"""

import math

pen = int(input())
shirts = list(map(int, input().split()))
t, p = map(int, input().split())

temp = 0
for i in range(6):
    temp += math.ceil(shirts[i]/t)

print(temp)
print(pen//p, pen%p)
