a = int(input())
num = []
while 1:
    if a%2 == 0:
        num.append(int(a))
        a /= 2
    elif a==1:
        num.append(int(a))
        break
    else:
        num.append(int(a))
        a = a*3 + 1


print(num)
