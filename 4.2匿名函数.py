'''
lambda
    匿名函数
    lanbda函数是一种快速定义单行的最小函数，是从lisp借用来的，
    可以用在任何需要函数的地方
'''
from functools import reduce

def f(x,y):
    return x+y

print(reduce(f,(1,2,3,4,5)))


ff = lambda x,y:x+y
print(ff(2,3))

#有上简化reduce为
print (reduce(lambda x,y:x+y,[1,2,3,4,5,6]))

'''
>>> foo  = [2,18,9,22,17,24,8,12,27]

    # filter 筛选foo数组里面 x%3 == 0 的值
>>> print filter(lambda x: x%3 == 0,foo)
[18,9,24,12,27]

====>> print [x for x in foo if x % 3 == 0]  #列表表达式（列表解析）

    # map 从foo里面依次取值进行 x*2+10的运算  
>>> print map(lambda x: x * 2 + 10,foo)
[14,46,28,54,44,58,26,34,64

====>> prin t[ x * 2 + 10 for x in foo]     #列表表达式（列表解析）

    # 同上
>>> print reduce(lambda x , y : x+y , foo)
139
'''