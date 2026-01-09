# 2754 학점계산
"""
    파이썬에는 switch가 없구나
    함수를 써보고 싶어서 억지로 짰는데 괜히 했나 싶기도 하고...
    함수 선언 위치 중요함!

"""

grade = input()

def plusmin(score):
    if(grade[1] == '+'):
        score += 0.3
    elif(grade[1] == '-'):
        score -= 0.3
    return score

if(grade[0] == 'A'):
    score = plusmin(4.0)
elif(grade[0] == 'B'):
    score = plusmin(3.0)
elif(grade[0] == 'C'):
    score = plusmin(2.0)
elif(grade[0] == 'D'):
    score = plusmin(1.0)
elif(grade[0] == 'F'):
    score = 0.0

print(score)


