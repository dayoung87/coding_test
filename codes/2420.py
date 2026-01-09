# 2420 사파리월드
""" 
    순간 공백 포함 입력 보고 머리가 멍해짐
    map() split() 함수의 존재 잊지 않기. < 어차피 하다보면 잊고 싶어도 잊을 수 없겠지만
"""

n, m = map(int, input().split())
print(abs(n-m))