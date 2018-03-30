# 解锁： yield 代替 return 

# 斐波纳挈数列

# 数列是一个递归数列，除第一个和第二个以外，任意一个数都由前两个数相加得到
from functools import reduce

def fb(x,y):
    return x+y

ff = [1,1]
for i in range(20):
    ff.append(fb(ff[i],ff[i+1]))

print(ff)

fff = [1,1]
for j in range(20):
    fff.append(reduce (lambda x,y:x+y,[fff[j],fff[j+1]]))

print(fff)

 #yield

def fbb(x,y):     
    yield x+y