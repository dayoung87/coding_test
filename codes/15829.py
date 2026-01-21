# 15829 Hashing
"""
    알고리즘 자체는 금방 떠올랐는데 ord() 함수를 떠올리지 못해서 책을 참고하였다.
"""

l = int(input())
word = input()
r = 31
m = 1234567891

result = 0

for i in range(l):
    result += (ord(word[i])-96) * r**i

print(result % m)