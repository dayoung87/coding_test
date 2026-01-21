# 1259 팰린드롬수

while True:
    num = input()
    t = len(num)

    if num == "0":
        break
    
    for i in range(t):
        if num[i] != num[t - i - 1]:
            print("no")
            break
    else:
        print("yes")   