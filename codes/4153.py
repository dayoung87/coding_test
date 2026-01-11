# 4153 직각삼각형
"""
    max 함수라는 좋은 것이 있었네요
    if 분기 순서를 잘못해서 몇 번 수정함
"""

while True:
    a, b, c = map(int, input().split())
    temp = max(a, b, c)

    if(a + b + c == 0):
        break
    elif(a**2 + b**2 + c**2 == 2 * temp**2):
        print("right")
    else:
        print("wrong")