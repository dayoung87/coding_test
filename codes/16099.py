# 16099 Larger Sport Facility
"""
    영어 지문 대충 읽고 풀다가 동점 처리 방법 못 봐서 틀림
"""

tnum = int(input())

for i in range(tnum):
    lt, wt, le, we = map(int, input().split())

    t = lt * wt
    e = le * we

    if(t > e):
        print("TelecomParisTech")
    elif(t == e):
        print("Tie")
    else:
        print("Eurecom")