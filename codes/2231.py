# 2231 분해합
"""
    자릿수를 어떻게 계산할까 고민하다가 자연로그 생각하고 나 천잰가?? 했는데
    문자열로 처리하면 됐었네... 그렇네...

    세상에 자릿수만 문자열이면 되는 게 아니라 n 자체를 문자열로 인덱스 접근하면 되는 거였잖아

    세상에 for-else 문이라는 것도 존재했군요..?
"""

n = int(input())

for m in range(1, n):
    total = m + sum(map(int, str(m)))
    if(total == n):
        print(m)
        break
else:
    print(0)